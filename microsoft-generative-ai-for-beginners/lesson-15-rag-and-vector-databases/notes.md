# Lesson 15: Retrieval Augmented Generation and Vector Databases

## Microsoft Course Concept

This lesson introduces Retrieval Augmented Generation and vector databases.

RAG improves LLM applications by connecting the model to an external knowledge base. Documents are ingested, chunked, embedded, stored, retrieved, and then used as context for answer generation.

## My Adaptation

I adapted the lesson into a local ResearchLab RAG workflow.

Instead of using Azure AI Search or Azure Cosmos DB immediately, I built a local vector index using sentence-transformers and scikit-learn NearestNeighbors. This avoids cloud paywalls while preserving the core RAG architecture.

## Key Concepts Practised

- Knowledge base creation
- Document ingestion
- Text chunking
- Embeddings
- Local vector index
- Nearest-neighbor retrieval
- RAG preparation
- Paywall-safe vector search

## Build Completed

Local RAG Knowledge Base Index Builder.

## Main Lesson

A RAG application is not just a chatbot. It requires a knowledge base, chunking strategy, embedding model, vector index, retrieval method, and evaluation process before the LLM generates grounded answers.

## Build 2: Local RAG Retriever

I built a local RAG retriever that loads the saved vector index, embeds a user query, searches the nearest document chunks, and returns the most relevant chunks with similarity scores.

This implements the retrieval stage of the RAG pipeline:

User query → query embedding → vector index search → retrieved context.
## Build 3: Local RAG + Claude Grounded Answer Generator

I built a full local RAG answer generator.

The app loads a local vector index, retrieves relevant chunks from the knowledge base, sends the retrieved context to Claude, and generates a grounded answer with supporting evidence and limitations.

This completes the core RAG pipeline:

Documents → chunks → embeddings → vector index → retrieval → context → grounded LLM answer.


## Build 4: RAG Evaluation Logger

I built a RAG evaluation logger.

The app retrieves relevant knowledge-base chunks, generates a grounded Claude answer, asks the user to score groundedness, relevance, and limitation quality, then logs the interaction into a CSV file.

This supports RAG evaluation by tracking questions, retrieved chunks, similarity scores, generated answers, evaluation scores, and user notes.

## Build 4: RAG Evaluation Logger

I built a RAG evaluation logger.

The app retrieves relevant knowledge-base chunks, generates a grounded Claude answer, asks the user to score groundedness, relevance, and limitation quality, then logs the interaction into a CSV file.

This supports RAG evaluation by tracking questions, retrieved chunks, similarity scores, generated answers, evaluation scores, and user notes.

## Lesson 15 Summary

This lesson completed the full RAG workflow:

Documents → chunks → embeddings → vector index → retrieval → grounded LLM answer → evaluation logging.

The main lesson is that a strong RAG application requires not only retrieval and generation, but also evaluation, logging, and continuous improvement.

