from typing import Optional

from fastapi import APIRouter, Query, status

from src.shared.logger import logging

from .manager import DashboardManager

dashboard_router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
)

dashboard_manager = DashboardManager()


@dashboard_router.get("/", status_code=status.HTTP_200_OK)
async def get_dashboard():
    logging.info("Get dashboard")

    return await dashboard_manager.get_dashboard()