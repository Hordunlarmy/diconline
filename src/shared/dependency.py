from typing import Annotated

from fastapi import Depends

from src.modules.auth.schemas import TokenData

from .auth import current_user

user_dependency = Annotated[TokenData, Depends(current_user)]
