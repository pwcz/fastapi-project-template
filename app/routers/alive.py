from fastapi import APIRouter

router = APIRouter()


@router.get("/alive", tags=["users"])
async def handle_alive():
    return {"status": "ok"}
