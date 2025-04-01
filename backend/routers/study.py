from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get('/health')
def vitals(message: str = "I'm gooood"):
    return {
        "message": 'googbli'
    }