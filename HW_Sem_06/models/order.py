from enum import Enum
from pydantic import BaseModel, Field, EmailStr
import datetime


class Status(Enum):
    assembly = 'В сборке'
    in_delivery = 'Передается в доставку'
    in_way = 'В пути'
    awaiting_receipt = 'Ожидает получения'
    received = 'Получен'
    cancelled = 'Отменён'


class Order(BaseModel):
    order_id: int
    creation_date: datetime.date
    status: Status
    user_id: int
    user_name: str
    user_surname: str
    user_email: EmailStr
    product_id: int
    product_title: str
    product_description: str
    product_price: float

    class Config:
        use_enum_values = True


class OrderIn(BaseModel):
    user_id: int = Field(..., title="User ID")
    product_id: int = Field(..., title="Product ID")
    creation_date: datetime.date = Field(..., title="Creation date")
    status: Status = Field(..., title="Order status")

    class Config:
        use_enum_values = True
