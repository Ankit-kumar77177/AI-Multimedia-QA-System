from fastapi import APIRouter

import app.routes.upload as upload

from app.services.summary_service import (
    generate_summary
)

router = APIRouter()

@router.get("/summary")
def summary():

    if not upload.uploaded_content:

        return {
            "summary": "No uploaded content found."
        }

    result = generate_summary(
        upload.uploaded_content
    )

    return {
        "summary": result
    } 