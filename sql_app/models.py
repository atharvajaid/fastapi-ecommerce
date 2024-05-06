# Import necessary dependencies
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    # Define the table name
    __tablename__ = "User"

    # Define columns
    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Product(Base):
    # Define the table name
    __tablename__ = "Product"

    # Define columns
    product_id = Column(String, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer,index=True)
  