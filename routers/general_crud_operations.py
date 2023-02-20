from fastapi import HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
import schemas, models
from fastapi import APIRouter
from repositories.general_crud_operation import \
    get_all_user, get_user_by_id, del_user_by_id, update_user_by_id, create_user
from oauth2 import get_current_user

router = APIRouter(
    prefix="/custom",
    tags=['Basic CRUD'],
)


@router.post("/create", )
async def create_userdata(userdata: schemas.UserDataSchema, db: Session = Depends(get_db)):
    return create_user(userdata, db)


@router.get("/all", status_code=200, )
def get_all(response: Response, db: Session = Depends(get_db),
            ## current_user: schemas.UserDataSchema = Depends(get_current_user)
            ):
    return get_all_user(response, db)


@router.get("/{id}", status_code=200, )
def user_by_id(id: int, db: Session = Depends(get_db)):
    print("ami");
    return get_user_by_id(id, db)


@router.delete("/delete/{id}", status_code=status.HTTP_200_OK, )
def delete__by_id(id: int, db: Session = Depends(get_db)):
    return del_user_by_id(id, db)


@router.put('/update/{id}', status_code=202, )
def update(
        updated_schema: schemas.UpdateUserDataSchema,
        id: int, db: Session = Depends(get_db, ),
        current_user: schemas.UserDataSchema = Depends(get_current_user)
):
    return update_user_by_id(updated_schema, id, db)
