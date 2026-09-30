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
│   │   ├── chatbot.py
│   │   └── students.py
│   │
│   ├── services/
│   │   ├── chatbot_service.py
│   │   └── vector_service.py
│   │
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
Get All Students
GET /api/students/

Get Student
GET /api/students/{student_id}

Update Student
PUT /api/students/{student_id}

Delete Student
DELETE /api/students/{student_id}

1.AI Chatbot
## AI Chatbot

The chatbot allows users to ask questions about student information.

### Endpoint

POST /api/chatbot/

### Example

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

2. Vector Database
## Vector Database

ChromaDB is used as the vector database for student-information retrieval.

It provides:

- Local storage
- Similarity-based search
- Simple Python integration
- Suitable integration with the chatbot workflow

The vector database is used for retrieval rather than blindly sending the complete database to the AI model.

3. Environment Variables
## Environment Variables

Create a `.env` file in the project root:

GEMINI_API_KEY=your_gemini_api_key

Never commit the `.env` file to GitHub.

4. Installation
## Installation

Clone the repository:

git clone https://github.com/rajanireddy08/student-database-backend.git

Enter the project directory:

cd student-database-backend

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

5. Run Locally
## Run Locally

Start the FastAPI server:

uvicorn app.main:app --reload

Open Swagger:

http://127.0.0.1:8000/docs

6. Run with Docker
## Run with Docker

Build the Docker image:

docker build -t student-database-backend .

Run the container:

docker run --name student-backend -p 8000:8000 --env-file .env student-database-backend

Open:

http://127.0.0.1:8000/docs

7. API Documentation
## API Documentation

FastAPI automatically provides interactive Swagger documentation at:

/docs

It can be used to test all Student and AI Chatbot APIs.

8. Security
## Security

- API keys are stored in environment variables.
- `.env` is excluded from Git.
- Database files are excluded from Git.
- ChromaDB files are excluded from Git.
- The chatbot is instructed not to invent student information.
- Only necessary student information is used for AI retrieval.

9. Testing
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

## Author

**Rajani N**

Student Database Management System – Backend