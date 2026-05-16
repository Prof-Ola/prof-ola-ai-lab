from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from pathlib import Path

# Load local embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Locate notes file
notes_path = Path(__file__).parent / "research_notes.txt"

if not notes_path.exists():
    print("ERROR: research_notes.txt was not found.")
    print(f"Expected location: {notes_path}")
    exit()

# Read notes
raw_text = notes_path.read_text(encoding="utf-8").strip()

if not raw_text:
    print("ERROR: research_notes.txt exists, but it is empty.")
    print(f"Please add research notes to: {notes_path}")
    exit()

# Split notes into chunks by paragraph
documents = [
    paragraph.strip()
    for paragraph in raw_text.split("\n\n")
    if paragraph.strip()
]

if len(documents) == 0:
    print("ERROR: No research notes were loaded.")
    print("Make sure each note is separated by a blank line.")
    exit()

# Create embeddings
document_embeddings = model.encode(documents)

print("\nResearch File Semantic Search App")
print(f"Loaded {len(documents)} research notes.")
print("Type 'exit' to stop.\n")

while True:
    query = input("Ask a research question: ")

    if query.lower() in ["exit", "quit", "stop"]:
        print("Search session ended.")
        break

    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1][:3]

    print("\nTop Results:\n")

    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. Similarity score: {similarities[index]:.3f}")
        print(documents[index])
        print()