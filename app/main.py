from fastapi import FastAPI

from .database import engine, Base
from .routers import students, chatbot


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Database Management System",
    description="Backend API for managing student information",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Student Database Backend is running",
        "docs": "/docs"
    }


# Student APIs
app.include_router(students.router)
app.include_router(chatbot.router)