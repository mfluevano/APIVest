# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI, Depends, HTTPException
from fastapi import status
#Data
from sqlalchemy.orm import Session
from sql_app  import crud, models, schemas
from sql_app.database import SessionLocal, engine


    
app = FastAPI(
    title="Vest Challenge Test API", 
    description="API for the VEST recruitment process", 
    version="1.0.1"
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"Hello": "World"}
    


@app.post("/trade/")
def trade(symbol:str, quantity: int, isbuy:bool, db: Session = Depends(get_db)):
    pass

@app.get("/operations")
def ger_operations(symbol:str, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users