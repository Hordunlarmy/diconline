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


@course_router.get("/students", status_code=status.HTTP_200_OK)
async def get_course_students(course_id: int = Query(None)):
    logging.info("Get course students")

    return await course_manager.get_course_students(course_id)


@course_router.post("/videos", status_code=status.HTTP_201_CREATED)
async def create_course_video(data: dict):
    logging.info("Create course video")

    return await course_manager.add_course_video(data)


@course_router.get("/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int):
    logging.info("Get course")

    return await course_manager.get_course(course_id)


@course_router.get("/{course_id}/students", status_code=status.HTTP_200_OK)
async def get_course_with_students(course_id: int):
    logging.info("Get course with students")

    return await course_manager.get_course_with_students(course_id)


@course_router.get("/{course_id}/videos", status_code=status.HTTP_200_OK)
async def get_course_videos(course_id: int):
    logging.info("Get course videos")

    return await course_manager.get_course_videos(course_id)
