from typing import Optional

from fastapi import APIRouter, Query, status

from .manager import DashboardManager

dashboard_router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
)

dashboard_manager = DashboardManager()


@dashboard_router.get("/", status_code=status.HTTP_200_OK)
async def get_dashboard():
    return await dashboard_manager.get_dashboard()


@dashboard_router.get("/department", status_code=status.HTTP_200_OK)
async def get_department_dashboard(
    page_size: Optional[int] = Query(10, ge=1, le=100),
    page: Optional[int] = Query(1, ge=1),
):
    return await dashboard_manager.get_department_dashboard(
        {
            "page": page,
            "page_size": page_size,
        }
    )


@dashboard_router.get("/student", status_code=status.HTTP_200_OK)
async def get_student_dashboard(student_id: Optional[int] = Query(None)):
    return await dashboard_manager.get_student_dashboard(student_id)
