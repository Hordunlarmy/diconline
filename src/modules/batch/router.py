from fastapi import APIRouter, status

from src.shared.logger import logging

from .manager import BatchManager

batch_router = APIRouter(
    prefix="/batches",
    tags=["batches"],
)

batch_manager = BatchManager()


@batch_router.get("/", status_code=status.HTTP_200_OK)
async def get_batches():
    logging.info("Get batches")

    return await batch_manager.get_batches()
