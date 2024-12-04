from typing import Optional

from fastapi import APIRouter, Query, status

from src.shared.logger import logging

from .manager import StudentManager

student_router = APIRouter(
    prefix="/students",
    tags=["students"],
)

student_manager = StudentManager()


@student_router.get("/", status_code=status.HTTP_200_OK)
async def get_students(
    page_size: Optional[int] = Query(10, ge=1, le=100),
    page: Optional[int] = Query(1, ge=1),
    status: Optional[str] = Query(None, max_length=50),
    order_by: Optional[str] = Query(None),
    sort_by: Optional[str] = Query(None),
):
    logging.info("Get students")

    return await student_manager.get_students(
        {
            "page": page,
            "page_size": page_size,
            "status": status,
            "sort_by": sort_by,
            "order_by": order_by,
        }
    )
