from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app_data = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app_data.post("/trade/",)
def create_user(user: schemas.operationBase, db: Session = Depends(get_db)):
    pass

@app_data.get("/operations")
def read_users(symbol, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# @app_data.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app_data.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app_data.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
