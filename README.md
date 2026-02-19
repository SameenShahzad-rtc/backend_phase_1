# Backend Phase 1
# Alembic Migrations 🚀  
*Database Schema Management with FastAPI*

This document provides step-by-step instructions for using **Alembic** to manage database migrations in a FastAPI project.  
Alembic helps track changes to your database schema in a versioned, controlled way.

---

## 📋 Table of Contents

- [Install Alembic](#install-alembic)  
- [Initialize Alembic](#initialize-alembic)  
- [Configure Alembic](#configure-alembic)  
- [Create a Migration](#create-a-migration)  
- [Apply Migration](#apply-migration)  
- [Revert Migration](#revert-migration)  
- [Tips & Best Practices](#tips--best-practices)  

---

### 🗓 Install Alembic

## Install Alembic using pip:


- pip install alembic
## 🗓 Initialize Alembic

Initialize Alembic inside your project:

alembic init migration


This will create a migration folder containing:

alembic.ini – configuration file

versions/ – folder for migration scripts

Note:
Each migration script in versions/ has a unique revision ID.

upgrade() → applies the changes

downgrade() → reverts the changes

## 🗓 Configure Alembic
Update alembic.ini

Set your database URL:

sqlalchemy.url = postgresql://username:password@localhost:5432/db_name

## Update alembic/env.py

Include your models and metadata:

from database import Base
from config.config import DATABASE_URL
from models.user import User
from models.project import Project
from models.task import Task

from sqlalchemy import engine_from_config, pool
from alembic import context

# Alembic Config object
config = context.config

# Set database URL
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Target metadata for autogenerate
target_metadata = Base.metadata

## 🗓 Create a Migration

Generate a new migration to add an age column:

alembic revision --autogenerate -m "add age column to user table"


Alembic will create a file in migration/versions/. Example content:

def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=False, server_default='20'))
   
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'age')

## 🗓 Apply Migration

Apply changes to the database:

alembic upgrade head


Check your database in pgAdmin 4:

The users table should now include the age column.

## 🗓 Revert Migration

To undo the last migration:

alembic downgrade -1


The age column will be removed from the users table.

