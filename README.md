# Student Database Management System – Backend

A modular backend application for managing student information through REST APIs, with an AI-powered chatbot using Gemini, LangGraph, and ChromaDB.

## Features

- Student CRUD operations
- SQLite database
- FastAPI REST APIs
- Pydantic data validation
- Swagger/OpenAPI documentation
- Duplicate email validation
- Gemini AI integration
- LangGraph chatbot workflow
- ChromaDB vector database
- Docker containerization
- Environment variable based secret management

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| SQLAlchemy | Database ORM |
| SQLite | Student database |
| Pydantic | Data validation |
| Gemini | AI response generation |
| LangGraph | AI workflow |
| ChromaDB | Vector search |
| Docker | Containerization |
| Swagger | API documentation |

## Project Structure

```text
student-database-backend/
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── chatbot.py
│   │   └── students.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chatbot_service.py
│   │   └── vector_service.py
│   │
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md

## Student APIs

### Create Student

POST /api/students/

Creates a new student in the database.

### Get All Students

GET /api/students/

Returns all students stored in the database.

### Get Student

GET /api/students/{student_id}

Returns the details of a specific student using the student ID.

### Update Student

PUT /api/students/{student_id}

Updates the details of an existing student.

### Delete Student

DELETE /api/students/{student_id}

Deletes a student from the database.

## AI Chatbot

The system includes an AI-powered chatbot that can answer questions about student information.

### Endpoint

POST /api/chatbot/

### Example Request

{
  "question": "Which students are in the CSE department?"
}

### Chatbot Flow

User Question
      ↓
FastAPI Chatbot API
      ↓
LangGraph
      ↓
ChromaDB Retrieval
      ↓
Relevant Student Information
      ↓
Gemini
      ↓
AI Generated Answer

## Vector Database

ChromaDB is used as the vector database for student-information retrieval.

It provides:

- Local storage
- Similarity-based search
- Simple Python integration
- Integration with the chatbot workflow

The vector database helps retrieve relevant student information before generating an AI response.

## Environment Variables

Create a `.env` file in the project root.

Add your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key

Never commit the `.env` file to GitHub.

## Installation

Clone the repository:

git clone https://github.com/rajanireddy08/student-database-backend.git

Enter the project directory:

cd student-database-backend

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

## Run Locally

Start the FastAPI server:

uvicorn app.main:app --reload

The application will run at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

http://127.0.0.1:8000/docs

Swagger can be used to test all Student APIs and the AI Chatbot API.

## Run with Docker

Build the Docker image:

docker build -t student-database-backend .

Run the Docker container:

docker run --name student-backend -p 8000:8000 --env-file .env student-database-backend

Open the Swagger documentation:

http://127.0.0.1:8000/docs

## Security

- API keys are stored using environment variables.
- The `.env` file is excluded from Git.
- Database files are excluded from Git.
- ChromaDB files are excluded from Git.
- The chatbot is instructed not to invent student information.
- Only necessary student information is used for AI retrieval.

## Testing

The following functionality has been tested:

- Student creation
- Duplicate email validation
- Get all students
- Get individual student
- Update student
- Delete student
- AI chatbot
- Swagger API documentation
- Dockerized FastAPI application