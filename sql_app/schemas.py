from typing import Union
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class User(BaseModel):
    email:str


class ProductCreate(BaseModel):
    title: str
    description: str
    price: int