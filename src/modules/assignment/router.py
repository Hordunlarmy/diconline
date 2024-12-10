from typing import Optional

from fastapi import APIRouter, Query, status

from src.shared.logger import logging

from .manager import AssignmentManager

assignment_router = APIRouter(
    prefix="/assignments",
    tags=["assignments"],
)

assignment_manager = AssignmentManager()


@assignment_router.get("/", status_code=status.HTTP_200_OK)
async def get_assignments(
    course_id: Optional[int] = Query(None),
):
    logging.info("Get assignments")

    return await assignment_manager.get_assignments(course_id)


@assignment_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_assignment(data: dict):
    logging.info("Create assignment")

    return await assignment_manager.create_assignment(data)


@assignment_router.get("/submissions", status_code=status.HTTP_200_OK)
async def get_submissions(
    assignment_id: Optional[int] = Query(None),
):
    logging.info("Get submissions")

    return await assignment_manager.get_assignment_submissions(assignment_id)


@assignment_router.get("/{assignment_id}", status_code=status.HTTP_200_OK)
async def get_assignment(assignment_id: int):
    logging.info("Get assignment")

    return await assignment_manager.get_assignment(assignment_id)


@assignment_router.put("/{assignment_id}", status_code=status.HTTP_200_OK)
async def update_assignment(assignment_id: int, data: dict):
    logging.info("Update assignment")

    return await assignment_manager.update_assignment(assignment_id, data)


@assignment_router.delete("/{assignment_id}", status_code=status.HTTP_200_OK)
async def delete_assignment(assignment_id: int):
    logging.info("Delete assignment")

    return await assignment_manager.delete_assignment(assignment_id)
