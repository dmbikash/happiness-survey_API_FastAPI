from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from hashing import Hash

import models
from database import get_db
from jwt_token import create_access_token
from fastapi.security import  OAuth2PasswordRequestForm

router = APIRouter(
    tags=["login"]
)


@router.post('/login', )
def login(request:  OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.UserDataModel).filter(models.UserDataModel.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Email -{request.username}-not found"
        )
    if not Hash.verify(request.password, user.password, ):  # request :not hashed  user:hashed
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="wrong password"
        )

    # token
    username = user.email
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub":  username},
        # expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

