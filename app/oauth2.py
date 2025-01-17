from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings
oauth2_scheme = OAuth2PasswordBearer(tokenUrl ='login')
#SECRET_KEY 
#Algorithms
#Expiration time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire =datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# def verify_access_token(token:str, credentials_exception):
#     try:

#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         print("Decoded payload:", payload)
#         id:str = payload.get("user_id")
#         print("Extracted user_id:", id)
#         if id is None:
#            raise credentials_exception
#         token_data = schemas.TokenData(id = id)
#     except JWTError:
#         raise credentials_exception
   
#     return token_data

from pydantic import ValidationError

def verify_access_token(token: str, credentials_exception):
    try:
        # Decode JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Decoded payload:", payload)

        # Extract user_id
        id = payload.get("user_id")

        if id is None:
            raise credentials_exception

# Convert id to string
        id = str(id)

        token_data = schemas.TokenData(id=id)

    except ValidationError as ve:
        print("Validation Error:", ve)
        raise credentials_exception
    except JWTError as e:
        print("JWT Error:", e)
        raise credentials_exception

    return token_data
def get_current_user(token: str= Depends(oauth2_scheme),db:Session =  Depends(database.get_db)):
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user= db.query(models.User).filter(models.User.id==token.id).first()
    return user 






