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
    student_id: Optional[int] = Query(None),
):
    logging.info("Get student courses")

    id = student_id if student_id else current_user.id
    return await student_manager.get_student_courses(id)


@student_router.get("/profile", status_code=status.HTTP_200_OK)
async def get_student_profile(
    current_user: user_dependency,
    student_id: Optional[int] = Query(None),
):
    logging.info("Get student profile")

    id = student_id if student_id else current_user.id
    return await student_manager.get_student_profile(id)


@student_router.get("/exams", status_code=status.HTTP_200_OK)
async def get_student_exams(
    current_user: user_dependency,
    student_id: Optional[int] = Query(None),
):
    logging.info("Get student exams")

    id = student_id if student_id else current_user.id
    return await student_manager.get_student_exams(id)


@student_router.get("/exams/results", status_code=status.HTTP_200_OK)
async def get_student_exam_results(
    current_user: user_dependency,
    student_id: Optional[int] = Query(None),
    exam_id: Optional[int] = Query(None),
):
    logging.info("Get student exam results")

    id = student_id if student_id else current_user.id
    return await student_manager.get_student_exam_result(exam_id, id)


@student_router.get("/assignments", status_code=status.HTTP_200_OK)
async def get_student_assignments(
    current_user: user_dependency,
    student_id: Optional[int] = Query(None),
):
    logging.info("Get student assignments")

    id = student_id if student_id else current_user.id
    return await student_manager.get_student_assignments(id)


@student_router.post("/assignments/submit", status_code=status.HTTP_200_OK)
async def submit_assignment(
    data: dict,
    current_user: user_dependency,
    student_id: Optional[int] = Query(None),
):
    logging.info("Get student assignment submissions")

    id = student_id if student_id else current_user.id
    return await student_manager.submit_assignment(id, data)
