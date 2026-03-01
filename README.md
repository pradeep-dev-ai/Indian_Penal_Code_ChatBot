⚖️ Indian Penal Code AI Assistant
Intelligent Legal Knowledge System Powered by Retrieval-Augmented Generation (RAG)
📌 Executive Summary

The Indian Penal Code (IPC) is the foundation of criminal law in India. However, navigating its extensive provisions can be time-consuming and challenging due to complex legal language and structural depth.

The Indian Penal Code AI Assistant is an enterprise-grade conversational system that leverages Retrieval-Augmented Generation (RAG) to provide accurate, contextual, and easy-to-understand explanations directly from the official IPC document.

This system enables users to query legal provisions using natural language while maintaining contextual conversation memory for multi-turn interactions.

🎯 Objectives

Provide structured access to IPC sections through natural language queries

Enable contextual legal explanations with source-backed retrieval

Maintain conversational memory for follow-up queries

Offer a scalable and modular architecture suitable for enterprise deployment

🏗️ System Architecture

The application follows a Retrieval-Augmented Generation pipeline:

Document Ingestion – Load official IPC PDF

Text Chunking – Recursive character-based splitting

Embedding Generation – OpenAI semantic embeddings

Vector Storage – ChromaDB persistence layer

Context Retrieval – Top-k semantic search

LLM Response Generation – GPT model with structured prompt

Conversation Memory – Session-based message history

Frontend Interface – Streamlit application

🧠 Core Capabilities

Context-aware legal question answering

Multi-turn conversational memory

Semantic search over legal text

Secure API key handling via environment configuration

Modular architecture for extensibility

🛠 Technology Stack
Layer	Technology
Frontend	Streamlit
Backend Framework	LangChain
Vector Database	ChromaDB
Embeddings	OpenAI text-embedding-3-small
LLM	GPT-based model
Language	Python
📂 Repository Structure
Indian_Penal_Code_ChatBot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── THE_INDIAN_PENAL_CODE.pdf
└── ipc_db/
🔐 Security & Configuration

Sensitive credentials are managed via environment variables.

Create a .env file:

OPENAI_API_KEY=your_openai_api_key

The .env file is excluded via .gitignore.

🚀 Installation & Deployment
1️⃣ Clone Repository
git clone https://github.com/pradeep-dev-ai/Indian_Penal_Code_ChatBot.git
cd Indian_Penal_Code_ChatBot
2️⃣ Create Virtual Environment
python -m venv rag
rag\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
streamlit run app.py
💬 Sample Queries

Which section deals with counterfeiting currency-notes?

What is the punishment under Section 302?

Define unlawful assembly under IPC.

Is Section 420 a cognizable offense?

📈 Enterprise Readiness

The system is designed with extensibility in mind:

Modular RAG pipeline

Replaceable vector database

Deployable on Streamlit Cloud or containerized environments

Scalable to other legal documents or multi-document corpora

⚠️ Disclaimer

This system provides informational responses derived from the Indian Penal Code document.
It does not constitute legal advice. For official guidance, consult a qualified legal professional.
