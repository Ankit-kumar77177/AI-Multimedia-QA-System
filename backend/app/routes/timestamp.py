from fastapi import APIRouter
from app.routes import upload

router = APIRouter()

@router.get("/timestamps")
async def get_timestamp():

    if not upload.uploaded_segments:

        return {
            "message": "No timestamps found"
        }

    segment = upload.uploaded_segments[0]

    return {
        "text": segment["text"],
        "start": segment["start"],
        "end": segment["end"],
        "file": upload.uploaded_file_path
    } 