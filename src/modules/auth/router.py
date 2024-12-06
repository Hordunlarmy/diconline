from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from src.shared.dependency import user_dependency
from src.shared.logger import logging

from .manager import AuthManager
from .schemas import CreateAccount, Token

auth_router = APIRouter(prefix="/auth", tags=["auth"])


auth_manager = AuthManager()


@auth_router.post(
    "/login", response_model=Token, status_code=status.HTTP_200_OK
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    logging.info("Login")

    return await auth_manager.login(form_data)


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(form_data: CreateAccount):
    logging.info("Register")

    return await auth_manager.register(form_data)


@auth_router.get("/user", status_code=status.HTTP_200_OK)
async def get_user(
    current_user: user_dependency,
):
    logging.info("Get user")

    return await auth_manager.get_user(current_user.id)
