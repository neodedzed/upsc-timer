from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.study import study

app = FastAPI()
app.include_router(study, prefix='/study')

@app.get('/health/')
def send_healthy(health_string = "HULAAA"):
    return {
        'message': health_string
    }