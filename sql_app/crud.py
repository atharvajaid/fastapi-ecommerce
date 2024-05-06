# Import necessary dependencies
from sqlalchemy.orm import Session
from . import models, schemas
from uuid import uuid4

# Function to retrieve a user by user_id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

# Function to retrieve a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Function to retrieve all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).all()

def create_user(db: Session,user_data: schemas.UserCreate):
    fake_hashed_password = user_data.password + "notreallyhashed"
    db_user = models.User(email=user_data.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    return db_user

# Function to retrieve all products
def get_products(db: Session, skip: str = 0, limit: str = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

# Function to retrieve a product by its ID
def get_product_by_id(db: Session,id: str):
    return db.query(models.Product).filter(models.Product.product_id==id).first()

def create_product(product:schemas.ProductCreate, db: Session):
    product_model = models.Product(product_id=str(uuid4())[:6], # Generate a unique product ID
        title=product.title, description=product.description,price=product.price)  # Create a new product instance
    db.add(product_model) # Add the product to the database session
    db.commit()
    return product_model

# Function to update an existing product
def update_product(product:schemas.ProductCreate,id:str,db:Session):
    product_model=db.query(models.Product).filter(models.Product.product_id == id).first()
    product_model.title=product.title # Update product title
    product_model.description=product.description # Update product description
    product_model.price=product.price # Update product price
    db.commit()
    return product_model

# Function to delete a product by its ID
def delete_product(id:str,db:Session):
    product_model=db.query(models.Product).filter(models.Product.product_id == id).first()
    db.delete(product_model) # Delete the product from the database session
    db.commit()

   