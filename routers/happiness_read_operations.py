from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter
from repositories .happiness_read_operations import get_user1,get_user2,get_user3,get_user4,get_user5

router = APIRouter(
    prefix="/read",
    tags=['Happy Read '],
)


@router.get("/vhappy", status_code=200, )
def user(db: Session = Depends(get_db)):
    # print("ami");
    return get_user1(db)


@router.get("/happy", status_code=200, )
def user(db: Session = Depends(get_db)):
    # print("ami");
    return get_user2(db)


@router.get("/neutral", status_code=200, )
def user(db: Session = Depends(get_db)):
    # print("ami");
    return get_user3(db)


@router.get("/sad", status_code=200, )
def user(db: Session = Depends(get_db)):
    # print("ami");
    return get_user4(db)


@router.get("/vsad", status_code=200, )
def user(db: Session = Depends(get_db)):
    # print("ami");
    return get_user5(db)

