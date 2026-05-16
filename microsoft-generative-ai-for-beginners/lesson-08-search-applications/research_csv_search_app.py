from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import pandas as pd
import numpy as np

# --------------------------------------------------
# Lesson 08 Build 3: CSV-Based Literature Search App
# ResearchLab version using BAAI BGE-small embeddings
# --------------------------------------------------

MODEL_NAME = "BAAI/bge-small-en-v1.5"

csv_path = Path(__file__).parent / "research_literature.csv"

if not csv_path.exists():
    print("ERROR: research_literature.csv was not found.")
    print(f"Expected location: {csv_path}")
    exit()

# Load CSV
df = pd.read_csv(csv_path)

required_columns = ["Title", "Topic", "Crop", "Method", "Finding", "Context"]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print("ERROR: Missing required columns:")
    print(missing_columns)
    exit()

if df.empty:
    print("ERROR: research_literature.csv is empty.")
    exit()

# Combine structured fields into searchable text
df["SearchText"] = (
    "Title: " + df["Title"].fillna("") + ". " +
    "Topic: " + df["Topic"].fillna("") + ". " +
    "Crop: " + df["Crop"].fillna("") + ". " +
    "Method: " + df["Method"].fillna("") + ". " +
    "Finding: " + df["Finding"].fillna("") + ". " +
    "Context: " + df["Context"].fillna("") + "."
)

documents = df["SearchText"].tolist()

print("\nLoading embedding model...")
model = SentenceTransformer(MODEL_NAME)

# Embed all CSV records
document_embeddings = model.encode(documents, normalize_embeddings=True)

print("\nResearch CSV Semantic Search App")
print(f"Model: {MODEL_NAME}")
print(f"Loaded {len(df)} research records.")
print("Type 'exit' to stop.\n")

while True:
    query = input("Ask a research question: ")

    if query.lower().strip() in ["exit", "quit", "stop"]:
        print("Search session ended.")
        break

    if not query.strip():
        print("Please enter a valid research question.\n")
        continue

    # BGE retrieval query prefix
    search_query = f"Represent this sentence for searching relevant passages: {query}"

    query_embedding = model.encode([search_query], normalize_embeddings=True)

    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1][:5]

    print("\nTop Results:\n")

    for rank, index in enumerate(top_indices, start=1):
        row = df.iloc[index]

        print(f"{rank}. {row['Title']}")
        print(f"Similarity score: {similarities[index]:.3f}")
        print(f"Topic: {row['Topic']}")
        print(f"Crop: {row['Crop']}")
        print(f"Method: {row['Method']}")
        print(f"Finding: {row['Finding']}")
        print(f"Context: {row['Context']}")
        print("-" * 80)