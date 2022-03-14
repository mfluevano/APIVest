from sqlalchemy.orm import Session

from . import models, schemas


def get_operations(db: Session):
    return db.query(models.Operations).all()


def get_operation_by_symbol(db: Session, symbol: str):
    return db.query(models.Operations).filter(models.Operations.symbol == symbol).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def trade_symbol(db: Session, symbol: str, quantity: int, isbuy: bool):
    #check if symbol exists in nasdaq
    

    operations_client = get_operation_by_symbol(db, symbol) 
    if operations_client is None:
        
    if isbuy == True:
        operation = "buy"
    else:
        operation = "sell"
        
    db_trade = models.Operations(symbol=symbol, company_name=operations_client.company_name, price=operations_client.price, quantity=quantity, date=operations_client.date, profit_loss=operations_client.profit_loss, operation=operation, total_stock_value=operations_client.total_stock_value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
