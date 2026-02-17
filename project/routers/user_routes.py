from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user_schema import UserRegister, UserLogin, Userout,LoginResponse,Token,TokenData
from security import get_pwd_hash,verify_password,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
r=APIRouter()





@r.post('/register',response_model=Userout)
def userReg(u:UserRegister,db:Session=Depends(get_db)):

    d_user=db.query(User).filter(User.email==u.email).first()
    if d_user:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="user already register")
    hashed_password = get_pwd_hash(u.password)
    n_user = User(
        username=u.username,
        email=u.email,
        password=hashed_password
    )
    db.add(n_user)
    db.commit()
    db.refresh(n_user)
    return n_user

# Users can login

@r.post('/login',response_model=Token)
def user_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):

    d_user = db.query(User).filter(User.username == form_data.username).first()

    if not d_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not registered"
        )

    if not verify_password(form_data.password, d_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid password"
        )
    access_token_expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"id": d_user.id, "username": d_user.username},
        expires_delta=access_token_expires,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message":"User is now logged in successfully"

    }
   
    