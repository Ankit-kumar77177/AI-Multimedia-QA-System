from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.upload import (
    router as upload_router
)

from app.routes.summary import (
    router as summary_router
)

from app.routes.timestamp import (
    router as timestamp_router
)

from app.routes.chat import (
    router as chat_router
)

app = FastAPI()

# SERVE UPLOADED FILES
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(summary_router)
app.include_router(timestamp_router)

@app.get("/")
def home():

    return {
        "message": "Backend Running Successfully"
    } 