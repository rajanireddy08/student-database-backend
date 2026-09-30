from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..database import get_db
from ..models import Student
from ..services.chatbot_service import build_chatbot


router = APIRouter(
    prefix="/api/chatbot",
    tags=["AI Chatbot"]
)


# Create chatbot
chatbot = build_chatbot()


# Request format
class ChatRequest(BaseModel):
    question: str


# Chatbot API
@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    # Get students from database
    students = db.query(Student).all()

    # Add students to ChromaDB
    from ..services.vector_service import add_students_to_vector_db

    add_students_to_vector_db(students)

    # Prepare student information
    if students:

        student_context = "\n".join(
            [
                (
                    f"ID: {student.id}, "
                    f"Name: {student.name}, "
                    f"Course: {student.course}, "
                    f"Department: {student.department}, "
                    f"Age: {student.age}"
                )
                for student in students
            ]
        )

    else:

        student_context = (
            "There are currently no students "
            "in the database."
        )

    # Send question and database information
    # to LangGraph
    result = chatbot.invoke(
        {
            "question": request.question,
            "student_context": student_context,
            "answer": ""
        }
    )

    return {
        "question": request.question,
        "answer": result["answer"]
    }