import chromadb


# Create a local ChromaDB database
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)


# Create or get the students collection
collection = chroma_client.get_or_create_collection(
    name="students"
)


def add_students_to_vector_db(students):
    """
    Add student information to ChromaDB.
    """

    if not students:
        return

    documents = []
    ids = []
    metadatas = []

    for student in students:

        # Information used for AI search
        document = (
            f"Student ID: {student.id}. "
            f"Name: {student.name}. "
            f"Age: {student.age}. "
            f"Course: {student.course}. "
            f"Department: {student.department}."
        )

        documents.append(document)

        ids.append(str(student.id))

        metadatas.append({
            "student_id": student.id,
            "name": student.name,
            "course": student.course,
            "department": student.department
        })

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )


def search_students(question: str, number_of_results: int = 5):
    """
    Search ChromaDB for students relevant to the question.
    """

    results = collection.query(
        query_texts=[question],
        n_results=number_of_results
    )

    return results.get("documents", [[]])[0]