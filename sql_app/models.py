from sqlalchemy import Boolean, Column, Integer, String, REAL
from sqlalchemy.orm import relationship

from .database import Base



class Operations(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    company_name = Column(String, index=True)
    price = Column(REAL, index=True)
    quantity = Column(Integer, index=True)
    date = Column(String, index=True)
    profit_loss = Column(REAL, index=True)
    operation = Column(String, index=True)
    total_stock_value = Column(REAL, index=True)





    
