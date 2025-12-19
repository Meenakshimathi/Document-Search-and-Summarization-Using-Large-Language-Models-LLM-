# Document-Search-and-Summarization-Using-Large-Language-Models-LLM-
The main objective of his assignment is to design a system that can search  and summarize vast amounts of textual data efficiently.
Document Search and Summarization using RAG (FAISS + LLM)

Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system for document search and summarization, built as part of an interview assignment.
The system allows users to:
Search a corpus of documents using semantic similarity
Retrieve the most relevant document chunks using FAISS
Generate concise, coherent summaries using a Large Language Model (LLM)
The solution is designed to be scalable, efficient, and interview-ready, with a clean architecture and clear evaluation strategy.


Architecture
User Query
↓
LLM-based Embeddings (Together AI)
↓
FAISS Vector Index (Semantic Search)
↓
Top-K Relevant Chunks
↓
LLM Summarization
↓
Final Answer / Summary

Project Structure

ragllm/
│
├── app.py # Streamlit UI
├── ingest.py # FAISS index creation
├── search.py # Vector search logic
├── summarize.py # RAG-based summarization
├── embeddings.py # LLM embedding generation
├── docs.npy # Stored document chunks
├── faiss.index # FAISS vector index
│
├── requirements.txt
└── README.md
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/7d02f52e-ee9b-4506-9e09-90b804880911" />
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/87d8c97d-a4d3-4813-8ec8-abc64d3021b3" />
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/a9c62a80-50f1-4ca8-8eb4-7568dfb8880d" />
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/6fdea9c2-45e1-4158-8c11-e13911a99d56" />
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/759d68d1-d040-4a98-81d1-0985fa22a2d5" />


Evaluation Strategy
🔹 Search Evaluation
Top-K relevance accuracy
Query-to-document matching

🔹 Summarization Evaluation
Automated metrics: ROUGE-1, ROUGE-L
Human qualitative assessment (coherence, coverage)

Conclusion
This project demonstrates a practical, production-oriented approach to document search and summarization using modern NLP techniques. 
It balances accuracy, scalability, and engineering robustness, making it suitable for both interview evaluation and real-world deployment.

