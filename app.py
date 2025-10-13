import streamlit as st
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch
from langchain_core.documents import Document
from langchain.chains import RetrievalQA
from langchain.llms.fake import FakeListLLM

# --- Configuration ---
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# --- Helper Functions ---

@st.cache_resource
def load_documents():
    """Loads text files from the data directory and creates Document objects."""
    documents = []
    for filename in os.listdir(DATA_PATH):
        if filename.endswith(".txt"):
            filepath = os.path.join(DATA_PATH, filename)
            with open(filepath, "r") as f:
                content = f.read()
                documents.append(Document(page_content=content, metadata={"source": filepath}))
    return documents

@st.cache_resource
def create_vector_store(_documents):
    """Creates a DocArrayInMemorySearch vector store from the documents."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    texts = text_splitter.split_documents(_documents)
    
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vector_store = DocArrayInMemorySearch.from_documents(texts, embeddings)
    return vector_store

# --- Main Application ---

st.title("VA Insights Engine Prototype")

# Load data and create vector store
documents = load_documents()
vector_store = create_vector_store(documents)

# User input
user_question = st.text_input("Ask a question about VA research:")

if st.button("Get Answer"):
    if user_question:
        # --- RAG Pipeline ---
        
        # 1. Retrieve relevant documents
        retriever = vector_store.as_retriever()
        
        # 2. Construct a prompt and use a placeholder LLM
        # In a real application, you would use a proper LLM like GPT-4
        responses = [
            "Based on the retrieved documents, the primary challenges with the DHR modernization were clinician burnout due to UI issues and increased documentation time. However, power users reported increased efficiency after an adjustment period.",
            "The analysis of telehealth adoption among rural veterans shows a 40% increase in virtual appointments, driven by convenience. Key barriers include poor broadband access and lack of digital literacy.",
            "The comparative study on mental health services found no significant difference in PTSD symptom reduction between in-person and virtual therapy. Virtual groups reported higher psychological safety, while in-person groups felt a stronger sense of camaraderie."
        ]
        llm = FakeListLLM(responses=responses)

        # 3. Create the RAG chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
        )

        # 4. Get the answer and source documents
        result = qa_chain({"query": user_question})
        answer = result["result"]
        source_docs = result["source_documents"]

        # Display the results
        st.subheader("Answer:")
        st.write(answer)

        st.subheader("Sources:")
        for doc in source_docs:
            # Display the entire metadata dictionary to avoid KeyError and for debugging
            st.write(f"- {doc.metadata}")

    else:
        st.warning("Please enter a question.")
