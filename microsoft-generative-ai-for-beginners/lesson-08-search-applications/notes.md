# Lesson 08: Building Search Applications

## Microsoft Course Concept

This lesson introduces semantic search using embeddings. Embeddings convert text into numerical vectors that allow a search application to compare meaning rather than only matching keywords.

## My Adaptation

Instead of searching YouTube transcripts, I built a semantic search app for research notes related to postharvest technology, AI in agriculture, harvest maturity, edible coatings, and LMIC farming systems.

## Key Concepts Practised

* Semantic search
* Keyword search versus meaning-based search
* Text embeddings
* Vector representations
* Cosine similarity
* Local embedding models
* Ranking search results by similarity score

## Build Completed

Research Semantic Search App using sentence-transformers and cosine similarity.

## Main Lesson

A search application can convert both documents and user questions into vectors, compare them mathematically, and return the most relevant content based on meaning.



\## Build 4: CSV RAG Answer Generator



I built a mini-RAG app that searches a structured CSV literature database using local BGE-small embeddings, retrieves the most relevant records, and sends them to Claude to generate grounded answers.



The app successfully answered questions on tomato harvest maturity and AI adoption barriers in LMIC agriculture. It retrieved relevant records with high similarity scores and generated structured answers with direct responses, supporting evidence, practical implications, and limitations.



This demonstrates the full retrieval-augmented generation pipeline:



User question → semantic search → retrieved records → grounded AI answer.

