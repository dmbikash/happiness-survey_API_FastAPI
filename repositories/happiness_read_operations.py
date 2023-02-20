from fastapi import status, Response, HTTPException
from sqlalchemy.orm import Session
import models


def get_user1(db):
    user = db.query(models.VHappyModel).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Ratings Found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{
        #     f"User id: {id} not Found"
        # }
    return user


def get_user2(db):
    user = db.query(models.HappyModel).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Ratings Found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{
        #     f"User id: {id} not Found"
        # }
    return user


def get_user3(db):
    user = db.query(models.NeutralModel).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Ratings Found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{
        #     f"User id: {id} not Found"
        # }
    return user


def get_user4(db):
    user = db.query(models.SadModel).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Ratings Found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{
        #     f"User id: {id} not Found"
        # }
    return user


def get_user5(db):
    user = db.query(models.VSadModel).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Ratings Found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{
        #     f"User id: {id} not Found"
        # }
    return user
