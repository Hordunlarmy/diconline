from datetime import datetime, timedelta, timezone
from typing import Annotated

from decouple import config
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from src.modules.auth.schemas import Token, TokenData

SECRET_KEY = config(
    "SECRET_KEY",
    default="cee619cd280708255b2ea19f56d24931d055d4148a8ed18688c962",
)
ALGORITHM = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config("token_expire", default=10, cast=int)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin/")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(email: str, password: str):

    from src.shared.manager import BaseManager

    user = await BaseManager.account_exists(email=email)

    if not user:
        return False

    if not verify_password(password, user["password"]):
        return False

    return user


def login_user(remember_me, data):
    persist = ACCESS_TOKEN_EXPIRE_MINUTES
    if remember_me:
        persist = timedelta(days=30)

    access_token = create_access_token(data, persist)

    return Token(access_token=access_token, token_type="bearer")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def decode_token(token):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
        )
    except JWTError:
        raise credentials_exception


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = await decode_token(token)
        user = TokenData(**payload)
        if user.id is None:
            raise credentials_exception
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def current_user(
    current_user: Annotated[TokenData, Depends(get_current_user)],
):
    user_data = current_user
    if user_data is None:
        user_data["authenticated"] = False
        raise HTTPException(status_code=400, detail="Inactive user")
    return user_data
