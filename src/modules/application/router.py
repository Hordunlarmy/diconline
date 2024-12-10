from typing import Optional

from fastapi import APIRouter, File, Form, Query, UploadFile, status

from src.shared.logger import logging

from .manager import ApplicationManager

application_router = APIRouter(
    prefix="/applications",
    tags=["PG Application"],
)

application_manager = ApplicationManager()


@application_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_application(
    first_name: Optional[str] = Form(None),
    last_name: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    gender: Optional[str] = Form(None),
    dob: Optional[str] = Form(None),
    program_id: Optional[str] = Form(None),
    photo: Optional[UploadFile] = File(None),
    application_form: Optional[UploadFile] = File(None),
):
    logging.info("Create Application")

    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "gender": gender,
        "dob": dob,
        "program_id": program_id,
        "photo": photo or None,
        "application_form": application_form or None,
    }

    return await application_manager.create_application(data)


@application_router.get("/", status_code=status.HTTP_200_OK)
async def get_applications(
    page_size: Optional[int] = Query(10, ge=1, le=100),
    page: Optional[int] = Query(1, ge=1),
    status: Optional[str] = Query(None, max_length=50),
):
    logging.info("Get Applications")

    return await application_manager.get_applications(
        {"page": page, "page_size": page_size, "status": status}
    )


@application_router.get("/{application_id}", status_code=status.HTTP_200_OK)
async def get_application(application_id: int):
    logging.info("Get Application")

    return await application_manager.get_application(application_id)


@application_router.post(
    "/{application_id}/approve", status_code=status.HTTP_200_OK
)
async def approve_application(application_id: int):
    logging.info("Approve Application")

    return await application_manager.approve_application(application_id)
