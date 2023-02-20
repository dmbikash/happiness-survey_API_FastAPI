from fastapi import HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
import schemas, models
from fastapi import APIRouter
from repositories .happiness_write_operations import post_rating1,post_rating2,post_rating3,post_rating4,post_rating5

router = APIRouter(
    prefix="/write",
    tags=['Happy Write'],
)


@router.post("/vhappy", )
async def post_rating_(userdata: schemas.HappySchema, db: Session = Depends(get_db)):
    return post_rating1(userdata, db)


@router.post("/happy", )
async def post_rating_(userdata: schemas.HappySchema, db: Session = Depends(get_db)):
    return post_rating2(userdata, db)


@router.post("/neutral", )
async def post_rating_(userdata: schemas.HappySchema, db: Session = Depends(get_db)):
    return post_rating3(userdata, db)

@router.post("/sad", )
async def post_rating_(userdata: schemas.HappySchema, db: Session = Depends(get_db)):
    return post_rating4(userdata, db)


@router.post("/vsad", )
async def post_rating_(userdata: schemas.HappySchema, db: Session = Depends(get_db)):
    return post_rating5(userdata, db)


