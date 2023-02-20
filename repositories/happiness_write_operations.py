from fastapi import status, Response, HTTPException
from sqlalchemy.orm import Session
import models


def post_rating1(userdata, db):
    new_user = models.VHappyModel(
        employeeID=userdata.employeeID
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def post_rating2(userdata, db):
    new_user = models.HappyModel(
        employeeID=userdata.employeeID
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def post_rating3(userdata, db):
    new_user = models.NeutralModel(
        employeeID=userdata.employeeID
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def post_rating4(userdata, db):
    new_user = models.SadModel(
        employeeID=userdata.employeeID
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def post_rating5(userdata, db):
    new_user = models.VSadModel(
        employeeID=userdata.employeeID
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



