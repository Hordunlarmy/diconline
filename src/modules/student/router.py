from typing import Optional

from fastapi import APIRouter, Query, status

from src.shared.dependency import user_dependency
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


@student_router.get("/courses", status_code=status.HTTP_200_OK)
async def get_student_courses(
    current_user: user_dependency,
):
    logging.info("Get student courses")

    return await student_manager.get_student_courses(current_user.id)


@student_router.get("/profile", status_code=status.HTTP_200_OK)
async def get_student_profile(
    current_user: user_dependency,
):
    logging.info("Get student profile")

    return await student_manager.get_student_profile(current_user.id)


@student_router.get("/exams", status_code=status.HTTP_200_OK)
async def get_student_exams(
    current_user: user_dependency,
):
    logging.info("Get student exams")

    return await student_manager.get_student_exams(current_user.id)


@student_router.get("/exams/results", status_code=status.HTTP_200_OK)
async def get_student_exam_results(
    current_user: user_dependency,
    exam_id: Optional[int] = Query(None),
):
    logging.info("Get student exam results")

    return await student_manager.get_student_exam_result(
        exam_id, current_user.id
    )


@student_router.get("/assignments", status_code=status.HTTP_200_OK)
async def get_student_assignments(
    current_user: user_dependency,
):
    logging.info("Get student assignments")

    return await student_manager.get_student_assignments(current_user.id)
