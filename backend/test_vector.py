from app.services.vector_service import (
    add_documents,
    search_documents
)

docs = [
    "Artificial Intelligence is the future.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks."
]

add_documents(docs)

result = search_documents("What is AI?")

print(result)