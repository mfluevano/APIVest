
# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status
#Data
from sqlalchemy.orm import Session
from sql_app  import crud, models, schemas
from services import nasdaq_service
from sql_app.database import SessionLocal, engine
import httpx

app = FastAPI(
    title="Vest Challenge Test API", 
    description="API for the VEST recruitment process", 
    version="1.0.1"
    )

# CORS
origins = [
    "https://api.nasdaq.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"hi": "Vest Challenge Test API"}
    

@app.post("/trade/")
async def trade(symbol:str, quantity: int, isbuy:bool, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        nasdaq_client = await nasdaq_service.checkSymbol(symbol)
        if nasdaq_client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Symbol not found")
        else:
            operations_client =  crud.get_operation_by_symbol(db, symbol)
            
            crud.trade_symbol(db, symbol, quantity, isbuy, nasdaq_client)
            
            
            
                
            
    
@app.get("/operations/{symbol}", status_code=status.HTTP_200_OK)")
def ger_operations(symbol:str, db: Session = Depends(get_db)):
    operations_client =  crud.get_operations(db, symbol)
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/history/{symbol}", status_code=status.HTTP_200_OK)")
async def get_operations(symbol:str, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        nasdaq_client = await nasdaq_service.get_history(symbol)
        if nasdaq_client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Symbol not found")
        else:
            data = nasdaq_client.json()
            data.sort(key=lambda x: x['t'])
            return data