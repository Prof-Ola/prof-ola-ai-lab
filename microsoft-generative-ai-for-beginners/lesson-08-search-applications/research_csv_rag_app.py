from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import numpy as np
import os

# --------------------------------------------------
# Lesson 08 Build 4: CSV Search + AI Answer Generator
# ResearchLab mini-RAG app using:
# 1. BAAI BGE-small embeddings for local semantic search
# 2. Claude API for grounded answer generation
# --------------------------------------------------

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")

if not ANTHROPIC_API_KEY:
    print("ERROR: ANTHROPIC_API_KEY was not found. Check your .env file.")
    exit()

client = Anthropic(api_key=ANTHROPIC_API_KEY)

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"

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
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

document_embeddings = embedding_model.encode(documents, normalize_embeddings=True)

print("\nResearch CSV RAG App")
print(f"Embedding model: {EMBEDDING_MODEL_NAME}")
print(f"Answer model: {ANTHROPIC_MODEL}")
print(f"Loaded {len(df)} research records.")
print("Type 'exit' to stop.\n")


def search_csv(query, top_k=5):
    """Search the CSV records using semantic similarity."""

    search_query = f"Represent this sentence for searching relevant passages: {query}"

    query_embedding = embedding_model.encode([search_query], normalize_embeddings=True)
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []

    for index in top_indices:
        row = df.iloc[index]

        results.append({
            "score": float(similarities[index]),
            "title": row["Title"],
            "topic": row["Topic"],
            "crop": row["Crop"],
            "method": row["Method"],
            "finding": row["Finding"],
            "context": row["Context"]
        })

    return results


def build_context(results):
    """Convert search results into context for Claude."""

    context_blocks = []

    for i, item in enumerate(results, start=1):
        block = f"""
Source {i}
Title: {item['title']}
Similarity score: {item['score']:.3f}
Topic: {item['topic']}
Crop: {item['crop']}
Method: {item['method']}
Finding: {item['finding']}
Context: {item['context']}
"""
        context_blocks.append(block.strip())

    return "\n\n".join(context_blocks)


def generate_answer(query, results):
    """Generate a grounded answer using Claude and retrieved CSV records."""

    context = build_context(results)

    prompt = f"""
You are ResearchLab AI, an academic research assistant.

Answer the user's question using only the retrieved research records below.

Important rules:
- Do not invent citations, statistics, author names, or claims.
- If the retrieved records are insufficient, say so clearly.
- Ground your answer in the provided records.
- Keep the answer concise, structured, and academically useful.
- Mention the relevant methods, crops, contexts, and limitations where appropriate.

User question:
{query}

Retrieved research records:
{context}

Please provide:
1. A direct answer.
2. Key supporting evidence from the retrieved records.
3. Practical implication for postharvest research or LMIC horticultural systems.
4. Any limitation of the available evidence.
"""

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=1200,
        temperature=0.3,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


while True:
    query = input("Ask a research question: ")

    if query.lower().strip() in ["exit", "quit", "stop"]:
        print("RAG session ended.")
        break

    if not query.strip():
        print("Please enter a valid research question.\n")
        continue

    try:
        results = search_csv(query, top_k=5)

        print("\nRetrieved Records:\n")

        for rank, item in enumerate(results, start=1):
            print(f"{rank}. {item['title']}")
            print(f"Similarity score: {item['score']:.3f}")
            print(f"Method: {item['method']}")
            print(f"Finding: {item['finding']}")
            print("-" * 80)

        answer = generate_answer(query, results)

        print("\nGrounded AI Answer:\n")
        print(answer)
        print()

    except Exception as e:
        print("\nSomething went wrong:")
        print(e)
        print()