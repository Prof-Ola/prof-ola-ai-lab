from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --------------------------------------------------
# Lesson 08: Semantic Search Application
# ResearchLab version using BAAI BGE-small embeddings
# --------------------------------------------------

MODEL_NAME = "BAAI/bge-small-en-v1.5"

print("\nLoading embedding model...")
model = SentenceTransformer(MODEL_NAME)

# Small research knowledge base
documents = [
    {
        "title": "Edible coatings and tomato shelf life",
        "text": "Edible coatings can reduce moisture loss, slow respiration, delay ripening, and extend the shelf life of tomatoes during postharvest storage."
    },
    {
        "title": "Computer vision for harvest maturity",
        "text": "Computer vision systems can classify fruit harvest maturity using external features such as colour, size, texture, and shape."
    },
    {
        "title": "Near-infrared spectroscopy for internal quality",
        "text": "Near-infrared spectroscopy can estimate internal fruit quality attributes such as soluble solids content, dry matter, firmness, and acidity."
    },
    {
        "title": "AI in resource-constrained farming systems",
        "text": "Smallholder farmers in low- and middle-income countries often face barriers such as limited cold storage, weak internet connectivity, high technology costs, and limited technical support."
    },
    {
        "title": "Warm-chain postharvest losses",
        "text": "Warm-chain conditions accelerate respiration, water loss, microbial decay, and quality deterioration in fresh horticultural crops."
    },
    {
        "title": "Mobile AI tools for farmers",
        "text": "Smartphone-based AI tools can support farmers by providing low-cost decision support for harvest timing, disease diagnosis, grading, and market readiness."
    }
]

# Extract document text
texts = [doc["text"] for doc in documents]

# Create document embeddings
# normalize_embeddings=True improves cosine similarity comparison
document_embeddings = model.encode(texts, normalize_embeddings=True)

print("\nResearch Semantic Search App")
print(f"Model: {MODEL_NAME}")
print(f"Loaded {len(documents)} research documents.")
print("Type 'exit' to stop.\n")

while True:
    query = input("Ask a research question: ")

    if query.lower().strip() in ["exit", "quit", "stop"]:
        print("Search session ended.")
        break

    if not query.strip():
        print("Please enter a valid research question.\n")
        continue

    # BGE models perform better when queries use this retrieval prefix
    search_query = f"Represent this sentence for searching relevant passages: {query}"

    # Create query embedding
    query_embedding = model.encode([search_query], normalize_embeddings=True)

    # Compare query with document embeddings
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    # Return top 3 results
    top_indices = np.argsort(similarities)[::-1][:3]

    print("\nTop Results:\n")

    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. {documents[index]['title']}")
        print(f"Similarity score: {similarities[index]:.3f}")
        print(f"{documents[index]['text']}\n")