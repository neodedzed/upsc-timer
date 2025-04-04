import datetime
from fastapi import APIRouter, Depends, FastAPI

from database.db import get_db
from database.models.Study_stats import Study_Time

study = APIRouter()

@study.get('/health')
def vitals(message: str = "I'm gooood"):
    return {
        "message": f'{message}, googbli'
    }

@study.get('/sessions')
def get_sessions(db = Depends(get_db)):
    start = datetime.datetime.now()
    results = db.query(Study_Time).all()

    print(results, f'\nTime taken {datetime.datetime.now()-start}')
    return results