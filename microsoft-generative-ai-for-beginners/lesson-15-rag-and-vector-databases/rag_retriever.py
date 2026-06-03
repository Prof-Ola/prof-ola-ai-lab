from pathlib import Path
import pickle
import json
import numpy as np
from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# Lesson 15 Build 2: Local RAG Retriever
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Load a local vector index, embed user queries, and retrieve
# the most relevant knowledge base chunks.
# --------------------------------------------------

MODEL_NAME = "BAAI/bge-small-en-v1.5"


def load_vector_index(index_dir):
    """
    Load embeddings, nearest-neighbor index, documents, and metadata.
    """

    embeddings_path = index_dir / "embeddings.npy"
    index_path = index_dir / "nearest_neighbors_index.pkl"
    documents_path = index_dir / "documents.json"
    metadata_path = index_dir / "index_metadata.json"

    missing_files = [
        path for path in [embeddings_path, index_path, documents_path, metadata_path]
        if not path.exists()
    ]

    if missing_files:
        print("ERROR: Missing index files:")
        for path in missing_files:
            print(path)
        print("\nRun rag_index_builder.py first.")
        exit()

    embeddings = np.load(embeddings_path)

    with open(index_path, "rb") as f:
        index = pickle.load(f)

    with open(documents_path, "r", encoding="utf-8") as f:
        documents = json.load(f)

    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    return embeddings, index, documents, metadata


def retrieve_chunks(query, model, index, documents, top_k=3):
    """
    Retrieve top matching chunks for a query.
    """

    search_query = f"Represent this sentence for searching relevant passages: {query}"
    query_embedding = model.encode([search_query], normalize_embeddings=True)

    # Prevent asking for more neighbours than available chunks
    safe_top_k = min(top_k, len(documents))

    distances, indices = index.kneighbors(query_embedding, n_neighbors=safe_top_k)

    results = []

    for distance, doc_index in zip(distances[0], indices[0]):
        similarity = 1 - float(distance)
        document = documents[doc_index]

        results.append({
            "similarity": round(similarity, 3),
            "distance": round(float(distance), 3),
            "source_file": document["source_file"],
            "chunk_id": document["chunk_id"],
            "text": document["text"]
        })

    return results


print("\nLocal RAG Retriever")
print("Lesson 15: Build 2")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
index_dir = base_dir / "vector_index"

embeddings, index, documents, metadata = load_vector_index(index_dir)

print("Loaded vector index.")
print(f"Embedding model in metadata: {metadata.get('embedding_model')}")
print(f"Number of chunks: {len(documents)}")

print("\nLoading embedding model...")
model = SentenceTransformer(MODEL_NAME)

while True:
    query = input("\nAsk a question: ")

    if query.lower().strip() in ["exit", "quit", "stop"]:
        print("RAG retriever ended.")
        break

    if not query.strip():
        print("Please enter a valid question.")
        continue

    results = retrieve_chunks(
        query=query,
        model=model,
        index=index,
        documents=documents,
        top_k=3
    )

    print("\nRetrieved Chunks:\n")

    for i, result in enumerate(results, start=1):
        print(f"{i}. Similarity: {result['similarity']}")
        print(f"Source: {result['source_file']}")
        print(f"Chunk ID: {result['chunk_id']}")
        print("Text:")
        print(result["text"])
        print("-" * 100)