from moviepy import VideoFileClip
from fastapi import APIRouter, UploadFile, File
import shutil
import os
import fitz
import whisper

from app.services.vector_service import (
    add_documents
)

router = APIRouter()

UPLOAD_DIR = "uploads"

model = whisper.load_model("base")

os.makedirs(UPLOAD_DIR, exist_ok=True)

# GLOBAL STORAGE
uploaded_content = ""
uploaded_segments = []
uploaded_file_path = ""

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    global uploaded_content
    global uploaded_segments

    file_path = f"{UPLOAD_DIR}/{file.filename}"
    global uploaded_file_path
    uploaded_file_path = file_path

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    text_content = ""

    # TXT SUPPORT
    if file.filename.endswith(".txt"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            text_content = f.read()

    # PDF SUPPORT
    elif file.filename.endswith(".pdf"):

        pdf = fitz.open(file_path)

        for page in pdf:

            text_content += page.get_text()

    # AUDIO SUPPORT
    elif (
        file.filename.endswith(".mp3")
        or file.filename.endswith(".wav")
    ):

        result = model.transcribe(file_path)

        uploaded_segments = result["segments"]

        text_content = result["text"]

    # VIDEO SUPPORT
    elif file.filename.endswith(".mp4"):

        video = VideoFileClip(file_path)

        audio_path = f"{file_path}.mp3"

        video.audio.write_audiofile(audio_path)

        result = model.transcribe(audio_path)

        uploaded_segments = result["segments"]

        text_content = result["text"]

    # SAVE CONTENT
    uploaded_content = text_content

    # ADD TO VECTOR DB
    if text_content:

        add_documents([text_content])

    return {
        "message": "File uploaded successfully"
    } 