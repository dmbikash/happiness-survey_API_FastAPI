
import models
from hashing import Hash


def create_new_user(user, db):
    new_user = models.UserDataModel(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user