from sqlalchemy import Boolean, Column, Integer, String, REAL
from sqlalchemy.orm import relationship

from .database import Base



class Operations(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    company_name = Column(String)
    price = Column(REAL)
    quantity = Column(Integer)
    date = Column(String)
    profit_loss = Column(REAL)
    operation = Column(String)
    total_stock_value = Column(REAL)
    consecutive = Column(Integer)





    
