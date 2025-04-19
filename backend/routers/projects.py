from fastapi import APIRouter, Depends

from crud.projects import add_project
from database.db import get_db
from database import Project
from database.schema.projects import ProjectCreate

project_route = APIRouter()

@project_route.get('/')
def get_all_projects(db = Depends(get_db)):
    results = db.query(Project).all()

    return results

@project_route.post('/project')
def post_new_project(project: ProjectCreate, db = Depends(get_db)):
    print('got here')
    add_project(db, project)

    
