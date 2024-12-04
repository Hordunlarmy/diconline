from fastapi import APIRouter, status

from src.shared.logger import logging

from .manager import DepartmentManager

department_router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)

department_manager = DepartmentManager()


@department_router.get("/", status_code=status.HTTP_200_OK)
async def get_departments():
    logging.info("Get departments")

    return await department_manager.get_departments()


@department_router.get("/{department_id}", status_code=status.HTTP_200_OK)
async def get_department(department_id: int):
    logging.info("Get department")

    return await department_manager.get_department(department_id)
