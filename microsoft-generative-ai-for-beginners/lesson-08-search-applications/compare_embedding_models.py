from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from pathlib import Path
import time

# Locate notes file
notes_path = Path(__file__).parent / "research_notes.txt"

if not notes_path.exists():
    print("ERROR: research_notes.txt was not found.")
    print(f"Expected location: {notes_path}")
    exit()

raw_text = notes_path.read_text(encoding="utf-8").strip()

if not raw_text:
    print("ERROR: research_notes.txt exists, but it is empty.")
    exit()

documents = [
    paragraph.strip()
    for paragraph in raw_text.split("\n\n")
    if paragraph.strip()
]

if len(documents) == 0:
    print("ERROR: No research notes were loaded.")
    exit()

# Models to compare
models_to_test = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "BAAI/bge-small-en-v1.5",
    "BAAI/bge-base-en-v1.5",
]

# Test questions
test_queries = [
    "What is optimum harvest time?",
    "How can AI help determine harvest maturity?",
    "What makes AI difficult to use in LMIC farming systems?",
    "Why do fruits deteriorate faster under warm-chain conditions?",
    "How can AI reduce postharvest losses?",
    "What technologies can measure internal fruit quality?",
    "How can farmers decide the best picking time?",
]

print("\nEmbedding Model Comparison")
print(f"Loaded {len(documents)} research notes.\n")

for model_name in models_to_test:
    print("=" * 80)
    print(f"Testing model: {model_name}")
    print("=" * 80)

    try:
        start_time = time.time()

        model = SentenceTransformer(model_name)

        # BGE models work better when retrieval queries are prefixed
        use_bge_prefix = model_name.startswith("BAAI/bge")

        document_embeddings = model.encode(documents, normalize_embeddings=True)

        load_and_embed_time = time.time() - start_time
        print(f"Model loaded and documents embedded in {load_and_embed_time:.2f} seconds.\n")

        for query in test_queries:
            search_query = f"Represent this sentence for searching relevant passages: {query}" if use_bge_prefix else query

            query_embedding = model.encode([search_query], normalize_embeddings=True)
            similarities = cosine_similarity(query_embedding, document_embeddings)[0]

            top_index = np.argmax(similarities)

            print(f"Query: {query}")
            print(f"Top score: {similarities[top_index]:.3f}")
            print(f"Top result: {documents[top_index]}")
            print("-" * 80)

    except Exception as e:
        print(f"FAILED for model: {model_name}")
        print(e)

    print("\n")