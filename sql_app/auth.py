# Import necessary dependencies
from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter,Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from pydantic import BaseModel
from starlette import status
from .models import User
from passlib.context import CryptContext
from .database import SessionLocal

# Create an APIRouter instance
router= APIRouter(
    prefix='/auth',
    tags=['auth']
)

# Secret key and algorithm for JWT
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

# Context for bcrypt hashing
bcrypt_context= CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

# Route to create a new user
@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,create_user_request:CreateUserRequest):
    # Check if user with given email already exists
    existing_user=db.query(User).filter(User.email==create_user_request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Hash the password and create a new user record
    create_user_model=User(email=create_user_request.email,hashed_password=bcrypt_context.hash(create_user_request.password),                       )
    db.add(create_user_model)
    db.commit()
    return {'detail': 'User created!', 'data':{create_user_model.email,create_user_model.user_id}}

# Route to login and get access token
@router.post("/token",response_model=Token)
async def login_for_access_token(db:db_dependency,form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    # Authenticate user with provided credentials
    user=authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user.')
    # Create and return access token
    token=create_access_token(user.email,user.user_id,timedelta(minutes=20))
    
    return {'access_token': token,'token_type':'bearer'}

# Function to authenticate user
def authenticate_user(email:str,password:str,db):
    # Query user from database by email
    user=db.query(User).filter(User.email==email).first()
    if not user:  
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

# Function to create JWT access token
def create_access_token(email:str,user_id:int,expire_delta:timedelta):
    encode={'sub':email,'id':user_id}
    expires=datetime.utcnow()+expire_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

# Dependency to get current user from JWT token
async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str=payload.get('sub')
        user_id:int =payload.get('id')
        if email is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user.')
        return {'email':email,'id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user.')
