from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.project import Project
from models.user import User
from schemas.project_schema import Projectinfo,Projectfind
from security import get_current_user
ro=APIRouter()


# Each project can have tasks
# # Tasks belong to a project
# pOST /projects
# GET /projects
# GET /projects/{id}
# DELETE /projects/{id}

@ro.post('/',response_model=Projectinfo)
def createProject(p:Projectfind,user:User=Depends(get_current_user), d : Session=Depends(get_db)):

    
    
    proj = Project(
        name=p.name,
        des=p.des,
        owner_id=user.id
    )
    
    d.add(proj)
    d.commit()
    d.refresh(proj)
    return proj

@ro.get('/',response_model=list[Projectinfo])
def Show_Projects(user:User=Depends(get_current_user), d : Session=Depends(get_db)):

    proj = d.query(Project).filter(Project.owner_id==user.id).all()

    return proj
@ro.get('/{id}',response_model=Projectinfo)
def Show_Projects(id:int,u:User=Depends(get_current_user), d : Session=Depends(get_db)):

   proj = d.query(Project).filter(
    Project.id == id,
    Project.owner_id == u.id
    ).first()
   if not proj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
   return proj

@ro.delete('/{id}')
def Del_Projects(id:int,u:User=Depends(get_current_user), d : Session=Depends(get_db)):

   proj = d.query(Project).filter( Project.id == id,
    Project.owner_id == u.id
   ).first()
   if not proj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
   d.delete(proj)
   d.commit()
   return {"msg":f"project {id} is deleted "}