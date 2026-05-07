from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.IndexFlatL2(384)

documents = []

# Default documents
default_docs = [
    "Artificial Intelligence is the future.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks."
]

def add_documents(text_chunks):

    embeddings = model.encode(text_chunks)

    index.add(
        np.array(embeddings).astype("float32")
    )

    documents.extend(text_chunks)

def search_documents(query):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype("float32"),
        k=3
    )

    results = []

    for i in I[0]:
        if i < len(documents):
            results.append(documents[i])

    return results

# Load default docs automatically
if len(documents) == 0:
    add_documents(default_docs) 