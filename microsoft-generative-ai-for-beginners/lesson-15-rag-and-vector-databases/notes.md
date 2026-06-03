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