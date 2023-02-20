from fastapi import FastAPI
import database
from routers import happiness_write_operations,happiness_read_operations

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

# app.include_router(user_registration.router)
# app.include_router(authentication.router)

# app.include_router(general_crud_operations.router)
# app.include_router(custom_delete.router)

app.include_router(happiness_read_operations.router)
app.include_router(happiness_write_operations.router)
