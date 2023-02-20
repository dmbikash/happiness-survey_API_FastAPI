import database, models


def delete():
    models.UserDataModel.__table__.drop(database.engine)
    database.Base.metadata.create_all(bind=database.engine)
    return "deleted"
