from fastapi import APIRouter
from pydantic import BaseModel

from app.services.vector_service import (
    search_documents
)

from app.services.chatbot_service import (
    ask_question
)

router = APIRouter()

class ChatRequest(BaseModel):

    question: str

@router.post("/chat")
def chat(req: ChatRequest):

    try:

        context = search_documents(
            req.question
        )

        answer = ask_question(
            context,
            req.question
        )

        return {
            "answer": answer
        }

    except Exception as e:

        print("CHAT ERROR:", e)

        return {
            "answer": f"Error: {str(e)}"
        } 