from sqlalchemy.orm import Session

from . import models, schemas


def get_operations(db: Session):
    operations = db.query(models.Operations).all()
    operations_list = []
    for operation in operations:
        operations_list.append({
            'symbol': operation.symbol,
            'company_name': operation.company_name,
            'price': operation.price,
            'quantity': operation.quantity,
            'date': operation.date,
            'profit_loss': operation.profit_loss,
            'operation': operation.operation,
            'total_stock_value': operation.total_stock_value
        })
    return operations_list



def get_operation_by_symbol(db: Session, symbol: str):
    return db.query(models.Operations).filter(models.Operations.symbol == symbol).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def trade_symbol(db: Session, symbol: str, quantity: int, isbuy: bool,nasdaq: dict):
    #count operations with symbol
    cant = db.query(models.Operations).filter(models.Operations.symbol == symbol).count()
    if cant > 0:
        last_price= db.query(models.Operations).filter(models.Operations.symbol == symbol).order_by(models.Operations.date.desc()).first().price
    if isbuy == False:
        if cant - quantity < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough shares")
        else:
            cant=cant-quantity      
            company_name = nasdaq['data']['companyName']
            price = nasdaq['data']['lastPrice']
            date = DateTime.now()
            # calculate profit_loss if is loss will be negative
            if price < last_price:
                profit_loss = (last_price - price) / last_price * 100 * quantity * -1
            else:
                
                profit_loss = (price - last_price) / last_price * 100 * quantity
            
            total_stock_value = price * quantity
    
        #add operation
            operation = models.Operations(symbol=symbol, company_name=company_name, price=price, quantity=quantity, date=date, profit_loss=profit_loss, operation=isbuy, total_stock_value=total_stock_value)
            db.add(operation)
            db.commit()
    else:
        cant=cant+quantity      
        company_name = nasdaq['data']['companyName']
        price = nasdaq['data']['lastPrice']
        date = DateTime.now()
        # calculate profit_loss if is loss will be negative
        if price < last_price:
            profit_loss = (last_price - price) / last_price * 100 * quantity * -1
        else:
            
            profit_loss = (price - last_price) / last_price * 100 * quantity
        
        total_stock_value = price * quantity
    
        #add operation
        operation = models.Operations(symbol=symbol, company_name=company_name, price=price, quantity=quantity, date=date, profit_loss=profit_loss, operation=isbuy, total_stock_value=total_stock_value)
        db.add(operation)
        db.commit()
    return operation