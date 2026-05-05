from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_sample():
    return {"message": "Starter working 🚀"}
