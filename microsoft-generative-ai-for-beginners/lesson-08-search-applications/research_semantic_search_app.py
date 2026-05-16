from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load a small local embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

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

# Extract document texts
texts = [doc["text"] for doc in documents]

# Create embeddings for the documents
document_embeddings = model.encode(texts)

print("\nResearch Semantic Search App")
print("Type 'exit' to stop.\n")

while True:
    query = input("Ask a research question: ")

    if query.lower() in ["exit", "quit", "stop"]:
        print("Search session ended.")
        break

    # Create embedding for the user query
    query_embedding = model.encode([query])

    # Compare query embedding with document embeddings
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    # Get top 3 most similar documents
    top_indices = np.argsort(similarities)[::-1][:3]

    print("\nTop Results:\n")

    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. {documents[index]['title']}")
        print(f"Similarity score: {similarities[index]:.3f}")
        print(f"{documents[index]['text']}\n")