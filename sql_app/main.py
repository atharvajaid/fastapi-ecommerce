# Import necessary dependencies
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.responses import JSONResponse
models.Base.metadata.create_all(bind=engine)
from .auth import router,get_current_user
from starlette import status
app = FastAPI()
app.include_router(router)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
user_dependency=Annotated[dict,Depends(get_current_user)]

# Endpoint to retrieve current user
@app.get("/",status_code=status.HTTP_200_OK)
async def user(user:user_dependency,db:Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return {'User':user}

# Endpoint to retrieve users
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    print(users)
    return users

# Endpoint to create a new product
@app.post("/products/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    # Create a product in the database
    product_data =crud.create_product(db=db,product=product)
    return {'detail': 'Product successfully created!', 'data':{
        'id':product_data.product_id,
        'title':product_data.title,
        'description':product_data.description,
        'price':product_data.price}}

# Endpoint to retrieve products
@app.get("/products/", )
def read_product(skip: str = 0, limit: str = 100, db: Session = Depends(get_db)):
    items = crud.get_products(db, skip=skip, limit=limit)
    print(items)
    return items

# Endpoint to retrieve a product by its ID
@app.get("/products/{product_id}",)
def read_product(product_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_product_by_id(db, id=product_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_user


@app.put("/products/{product_id}")
async def update_product(product_id: str,product:schemas.ProductCreate,db:Session=Depends(get_db)):
    # Get the product by its ID from the database
    db_user = crud.get_product_by_id(db, id=product_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Product not found")
    # Update the product in the database
    db_item = crud.update_product(db=db,id=product_id,product=product)
    return {'detail': 'Product successfully updated!', 'data':db_item}

# Endpoint to delete a product
@app.delete("/products/{product_id}")
async def delete_product(product_id: str,db:Session=Depends(get_db)):
    # Delete a product by its ID from the database
    db_item = crud.delete_product(id=product_id,db=db)
    return {"message": "Item deleted successfully"}