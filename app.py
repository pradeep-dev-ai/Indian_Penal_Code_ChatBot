import os
from dotenv import load_dotenv
import streamlit as st
from operator import itemgetter

# ==============================
# LOAD ENV
# ==============================

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(page_title="IPC Legal Assistant", layout="wide")
st.title("⚖️ Indian Penal Code Chatbot")

# ==============================
# LOAD & CACHE RAG SYSTEM
# ==============================

@st.cache_resource
def load_rag_system():

    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_core.runnables import RunnableLambda
    from langchain_core.prompts import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        SystemMessagePromptTemplate,
        MessagesPlaceholder
    )
    from langchain_core.output_parsers import StrOutputParser
    from langchain_community.chat_message_histories import ChatMessageHistory
    from langchain_core.runnables.history import RunnableWithMessageHistory

    # Load PDF
    loader = PyPDFLoader("THE_INDIAN_PENAL_CODE.pdf")
    documents = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # Embeddings
    embedding = OpenAIEmbeddings(model="text-embedding-3-small")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="ipc_db"
    )

    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    # Format docs
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retrieval_chain = retriever | RunnableLambda(format_docs)

    # Prompt
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are an AI-powered legal assistant specialized in the Indian Penal Code (IPC). "
            "Use the provided context to answer clearly and accurately."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template(
            """Answer the question based on the below context.
If context is missing, say 'I don't know'.

Context:
{context}

Question:
{question}"""
        )
    ])

    model = ChatOpenAI(model="gpt-5.2-2025-12-11")
    parser = StrOutputParser()

    # Proper RAG pipeline
    rag_chain = (
        {
            "context": itemgetter("question") | retrieval_chain,
            "question": itemgetter("question"),
            "chat_history": itemgetter("chat_history"),
        }
        | prompt
        | model
        | parser
    )

    # Memory store
    store = {}

    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    rag_with_memory = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="question",
        history_messages_key="chat_history"
    )

    return rag_with_memory


# Load system
rag_with_memory = load_rag_system()

# ==============================
# STREAMLIT CHAT UI
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==============================
# CHAT INPUT
# ==============================

if user_prompt := st.chat_input("Ask about IPC sections..."):

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = rag_with_memory.invoke(
                {"question": user_prompt},
                config={"configurable": {"session_id": "user1"}}
            )
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )