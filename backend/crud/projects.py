from sqlalchemy.orm import Session
from database.models.Projects import Project
from database.schema.projects import ProjectCreate

def get_projects(db: Session):
    return db.query(Project).all()

def add_project(db: Session, project: ProjectCreate):
    print('Attempting')
    print(project)
    project_insert = Project(project_name=project.project_name)
    db.add(project_insert)
    db.commit()
    return 'sucess'

    