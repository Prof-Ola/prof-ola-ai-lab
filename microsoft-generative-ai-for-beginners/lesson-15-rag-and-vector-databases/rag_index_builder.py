from pathlib import Path
import pickle
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors


# --------------------------------------------------
# Lesson 15 Build 1: Local RAG Knowledge Base Index Builder
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Build a local vector index from text files using chunking,
# embeddings, and nearest-neighbor search.
# --------------------------------------------------

MODEL_NAME = "BAAI/bge-small-en-v1.5"


def chunk_text(text, max_words=90, overlap_words=20):
    """
    Split text into overlapping chunks.
    """

    words = text.split()
    chunks = []

    if len(words) <= max_words:
        return [text.strip()] if text.strip() else []

    start = 0

    while start < len(words):
        end = start + max_words
        chunk = " ".join(words[start:end]).strip()

        if chunk:
            chunks.append(chunk)

        start += max_words - overlap_words

    return chunks


def load_text_documents(knowledge_base_dir):
    """
    Load all .txt files from the knowledge base folder.
    """

    documents = []

    txt_files = list(knowledge_base_dir.glob("*.txt"))

    for file_path in txt_files:
        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks, start=1):
            documents.append({
                "source_file": file_path.name,
                "chunk_id": f"{file_path.stem}_chunk_{i}",
                "text": chunk
            })

    return documents


def build_vector_index(documents, output_dir):
    """
    Generate embeddings and build nearest-neighbor index.
    """

    print("\nLoading embedding model...")
    model = SentenceTransformer(MODEL_NAME)

    texts = [
        f"Represent this passage for retrieval: {doc['text']}"
        for doc in documents
    ]

    print("Generating embeddings...")
    embeddings = model.encode(texts, normalize_embeddings=True)

    print("Building nearest-neighbor index...")
    index = NearestNeighbors(
        n_neighbors=min(5, len(documents)),
        metric="cosine",
        algorithm="brute"
    )

    index.fit(embeddings)

    output_dir.mkdir(parents=True, exist_ok=True)

    np.save(output_dir / "embeddings.npy", embeddings)

    with open(output_dir / "nearest_neighbors_index.pkl", "wb") as f:
        pickle.dump(index, f)

    with open(output_dir / "documents.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    metadata = {
        "embedding_model": MODEL_NAME,
        "number_of_documents": len(documents),
        "index_type": "NearestNeighbors cosine brute",
        "notes": "Local vector index for Lesson 15 RAG practice."
    }

    with open(output_dir / "index_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    return metadata


print("\nRAG Knowledge Base Index Builder")
print("Lesson 15: Retrieval Augmented Generation and Vector Databases\n")

base_dir = Path(__file__).parent
knowledge_base_dir = base_dir / "knowledge_base"
output_dir = base_dir / "vector_index"

if not knowledge_base_dir.exists():
    print("ERROR: knowledge_base folder was not found.")
    print(f"Expected location: {knowledge_base_dir}")
    exit()

documents = load_text_documents(knowledge_base_dir)

if not documents:
    print("ERROR: No text documents were loaded.")
    print("Add at least one .txt file to the knowledge_base folder.")
    exit()

print(f"Loaded {len(documents)} chunks from knowledge base.")

metadata = build_vector_index(
    documents=documents,
    output_dir=output_dir
)

print("\nVector index created successfully.\n")
print("Index metadata:")
print(json.dumps(metadata, indent=2))

print("\nGenerated files:")
print(output_dir / "embeddings.npy")
print(output_dir / "nearest_neighbors_index.pkl")
print(output_dir / "documents.json")
print(output_dir / "index_metadata.json")