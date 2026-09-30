import os
from typing import TypedDict

from dotenv import load_dotenv
from google import genai

from langgraph.graph import StateGraph, START, END

from .vector_service import search_students

# Load environment variables from .env
load_dotenv()

# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


# State used by LangGraph
class ChatState(TypedDict):
    question: str
    student_context: str
    answer: str


# Step 1: Retrieve student information
def retrieve_student_data(state: ChatState):

    question = state["question"]

    # Search ChromaDB for relevant student information
    results = search_students(question)

    if results:
        student_context = "\n".join(results)
    else:
        student_context = "No relevant student information was found."

    return {
        "student_context": student_context
    }


# Step 2: Generate answer using Gemini
def generate_answer(state: ChatState):

    question = state["question"]

    context = state.get(
        "student_context",
        "No student information was found."
    )

    prompt = f"""
You are a Student Database Assistant.

Answer the user's question using only the
student information provided below.

Student information:
{context}

User question:
{question}

Rules:
1. Do not invent student information.
2. If the requested information is not available,
   clearly say that it is not available.
3. Give a simple and clear answer.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

    except Exception as e:

        if "503" in str(e) or "UNAVAILABLE" in str(e):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        else:
            raise

    return {
        "answer": response.text
    }


# Create LangGraph workflow
def build_chatbot():

    workflow = StateGraph(ChatState)

    workflow.add_node(
        "retrieve",
        retrieve_student_data
    )

    workflow.add_node(
        "generate",
        generate_answer
    )

    workflow.add_edge(
        START,
        "retrieve"
    )

    workflow.add_edge(
        "retrieve",
        "generate"
    )

    workflow.add_edge(
        "generate",
        END
    )

    return workflow.compile()