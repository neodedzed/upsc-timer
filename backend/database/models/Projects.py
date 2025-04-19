from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Project(Base):
    __tablename__= 'projects'

    id = Column(Integer,primary_key=True, nullable=False)
    project_name = Column(String, nullable=False)

    work_time = relationship("WorkTime", back_populates='project', cascade='all, delete')

class WorkTime(Base):
    __tablename__ = 'work_times'

    id = Column(Integer, primary_key=True, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    start_times = Column(DateTime, nullable = False)
    end_times = Column(DateTime, nullable=True)
    
    project = relationship('Project', back_populates='work_time')


