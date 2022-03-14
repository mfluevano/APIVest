from pydantic import BaseModel


class operationBase(BaseModel):
    symbol: str
    company_name: str
    price: float
    quantity: int
    date: str
    profit_loss:   float
    operation: str
    total_stock_value: int