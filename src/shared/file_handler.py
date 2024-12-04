import logging
from typing import Optional

import cloudinary
from cloudinary import uploader
from decouple import config

from src.shared.error_handler import CustomError

logger = logging.getLogger(__name__)

cloudinary.config(
    cloud_name=config("CLOUD_NAME"),
    api_key=config("API_KEY"),
    api_secret=config("API_SECRET"),
    secure=True,
)


async def upload_file(file, folder: str = "files") -> Optional[str]:
    """Uploads a file to Cloudinary and returns the URL."""
    try:
        print(f"Uploading file to Cloudinary: {file.filename}")
        result = uploader.upload(
            file.file,
            folder=folder,
            resource_type="raw",
        )
        return result.get("secure_url")
    except Exception as e:
        logger.exception(f"Cloudinary Error: {e}")
        raise CustomError(f"Cloudinary Error: {e}", 400)
