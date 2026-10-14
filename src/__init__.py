from sqlmodel import SQLModel, Field
import uuid
from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum


class User(SQLModel, table= True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        default_factory= uuid.uuid4, primary_key = True
    )
    first_name: str
    last_name: Optional[str] = None
    email: str = Field(unique= True)
    password_hash: str
    role: str = Field(default= "client")
    is_verified: bool = Field(default= False)
    created_at: datetime = Field(default_factory= datetime.now)
    
class Product(SQLModel, table= True):
    __tablename__ = "products"
    uid: uuid.UUID = Field(
        default_factory= uuid.uuid4, primary_key = True
    )
    name: str
    description: Optional[str] = None
    price: Decimal = Field(max_digits=10, decimal_places=2)
    stock: int = Field(default= 0)
    is_active: bool = Field(default= True)
    created_at: datetime = Field(default_factory= datetime.now)

class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"
        
class Order(SQLModel, table=True):
    __tablename__ = "orders"
    uid: uuid.UUID = Field(
        default_factory= uuid.uuid4, primary_key = True
    )
    client_uid: uuid.UUID = Field(foreign_key="users.uid")
    status: OrderStatus = Field(default= OrderStatus.pending)
    created_at: datetime = Field(default_factory= datetime.now)
    
class OrderItem(SQLModel, table= True):
    __tablename__ = "orderitems"
    uid: uuid.UUID = Field(
        default_factory= uuid.uuid4, primary_key = True
    )
    order_uid: uuid.UUID = Field(foreign_key= "orders.uid")
    product_uid: uuid.UUID = Field(foreign_key= "products.uid")
    quantity: int = Field(ge=1)
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)