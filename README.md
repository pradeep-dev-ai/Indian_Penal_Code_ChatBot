# ⚖️ Indian Penal Code AI Assistant

> Intelligent Legal Knowledge System powered by Retrieval-Augmented Generation (RAG)

---

## 📌 Overview

The **Indian Penal Code (IPC)** forms the foundation of criminal law in India.  
However, navigating its extensive provisions can be complex due to legal terminology and structural depth.

The **Indian Penal Code AI Assistant** is an AI-powered chatbot that enables users to interact with the IPC using natural language queries. It leverages a **Retrieval-Augmented Generation (RAG)** architecture to provide context-aware and accurate responses directly from the official IPC document.

---

## 🚀 Key Features

- 🔎 Semantic search over IPC document
- 💬 Multi-turn conversational memory
- 📚 Context-aware legal explanations
- 🔐 Secure API key management
- 🧩 Modular and scalable architecture

---

## 🏗️ System Architecture

1. **Document Ingestion** – Load official IPC PDF  
2. **Text Chunking** – Recursive splitting  
3. **Embedding Generation** – OpenAI embeddings  
4. **Vector Storage** – ChromaDB  
5. **Context Retrieval** – Top-k semantic search  
6. **Response Generation** – GPT model  
7. **Conversation Memory** – Session-based history  

---

## 🛠️ Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | LangChain |
| Vector Database | ChromaDB |
| Embeddings | OpenAI `text-embedding-3-small` |
| LLM | GPT Model |
| Language | Python |

---

## 📂 Project Structure
```
Indian_Penal_Code_ChatBot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── THE_INDIAN_PENAL_CODE.pdf
└── ipc_db/
```
------
