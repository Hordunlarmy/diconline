from fastapi import APIRouter, status

from src.shared.logger import logging

from .manager import CourseManager

course_router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)

course_manager = CourseManager()


@course_router.get("/{program_id}", status_code=status.HTTP_200_OK)
async def get_courses(program_id: int = None):
    logging.info("Get courses")

    return await course_manager.get_courses(program_id)
