from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
from fastapi import APIRouter
from repositories.user_registration import create_new_user

router = APIRouter(
    prefix="/signup",
    tags=['User Registration']
)


@router.post('/', response_model=schemas.ShowUserInfo, )
def create_user(user: schemas.UserInfo, db: Session = Depends(get_db)):
    return create_new_user(user, db)

