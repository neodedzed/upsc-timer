from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = ['*']

from routers import projects, study
app = FastAPI()
app.include_router(study.study_route, prefix='/study')
app.include_router(projects.project_route, prefix = '/projects')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*']
    )

@app.get('/health/')
def send_healthy(health_string = "HULAAA"):
    return {
        'message': health_string
    }