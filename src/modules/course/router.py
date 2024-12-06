from fastapi import APIRouter, Query, status

from src.shared.logger import logging

from .manager import CourseManager

course_router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)

course_manager = CourseManager()


@course_router.get("/", status_code=status.HTTP_200_OK)
async def get_courses(program_id: int = Query(default=None)):
    logging.info("Get courses")

    return await course_manager.get_courses(program_id)


@course_router.get("/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int):
    logging.info("Get course")

    return await course_manager.get_course(course_id)


@course_router.get("/{course_id}/students", status_code=status.HTTP_200_OK)
async def get_course_with_students(course_id: int):
    logging.info("Get course with students")

    return await course_manager.get_course_with_students(course_id)
