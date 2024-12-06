from fastapi import APIRouter, status

from src.shared.logger import logging

from .manager import ProgramManager

program_router = APIRouter(
    prefix="/programs",
    tags=["programs"],
)

program_manager = ProgramManager()


@program_router.get("/{department_id}", status_code=status.HTTP_200_OK)
async def get_programs(department_id: int = None):
    logging.info("Get Programs")

    return await program_manager.get_programs(department_id)


@program_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_programs():
    logging.info("Get All Programs")

    return await program_manager.get_all_programs()
