from typing import Optional

from fastapi import APIRouter, Query, status

from src.shared.dependency import user_dependency
from src.shared.logger import logging

from .manager import StaffManager

staff_router = APIRouter(
    prefix="/staffs",
    tags=["staffs"],
)

staff_manager = StaffManager()


@staff_router.get("/", status_code=status.HTTP_200_OK)
async def get_staffs(
    page_size: Optional[int] = Query(10, ge=1, le=100),
    page: Optional[int] = Query(1, ge=1),
    status: Optional[str] = Query(None, max_length=50),
    order_by: Optional[str] = Query(None),
    sort_by: Optional[str] = Query(None),
):
    logging.info("Get staffs")

    return await staff_manager.get_staffs(
        {
            "page": page,
            "page_size": page_size,
            "status": status,
            "sort_by": sort_by,
            "order_by": order_by,
        }
    )


@staff_router.get("/profile", status_code=status.HTTP_200_OK)
async def get_staff(
    current_user: user_dependency,
    staff_id: Optional[int] = Query(None),
):
    logging.info("Get staff")

    id = staff_id if staff_id else current_user.id
    return await staff_manager.get_staff(id)


@staff_router.get("/courses", status_code=status.HTTP_200_OK)
async def get_staff_courses(
    current_user: user_dependency,
    staff_id: Optional[int] = Query(None),
):
    logging.info("Get staff courses")

    id = staff_id if staff_id else current_user.id
    return await staff_manager.get_staff_courses(id)
