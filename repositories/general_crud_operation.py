from fastapi import status, Response, HTTPException
from sqlalchemy.orm import Session
import models


def create_user(userdata, db):
    new_user = models.UserDataModel(
        name=userdata.name,
        email=userdata.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(response: Response, db: Session):
    all_user = db.query(models.UserDataModel).all()
    if not all_user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            f"User not Found"
        }
    return all_user


def get_user_by_id(id, db, ):
    user_by_id = db.query(models.UserDataModel).filter(models.UserDataModel.id == id).first()
    if not user_by_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User id: {id} not Found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{
        #     f"User id: {id} not Found"
        # }
    return user_by_id


def del_user_by_id(id, db):
    user_by_id = db.query(models.UserDataModel).filter(models.UserDataModel.id == id).first()
    if not user_by_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User id: {id} not Found"
        )
    else:
        db.query(models.UserDataModel).filter(models.UserDataModel.id == id).delete()
        db.commit()
    return "User was deleted successfully"


def update_user_by_id(updated_schema, id, db):
    find_user = db.query(models.UserDataModel).filter(models.UserDataModel.id == id)
    if find_user.first():
        print("find_user")
        print(find_user)
        find_user.update(updated_schema.dict())
        db.commit()
        return 'hoise'
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User id: {id} not Found"
        )
