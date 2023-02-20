
from repositories .custom_del import delete
from fastapi import APIRouter

router = APIRouter()


@router.delete("/DeleteTable", tags=['Special Custom Delete Operation'])
async def delete_table():
    return delete()
