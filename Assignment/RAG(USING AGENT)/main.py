from chromaretrival import chroma_retrieval
from langchain.agents import create_agent
from agent import llm, embeddings_model
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import tempfile
import streamlit as st

# ---------- Chroma ----------
client = chromadb.PersistentClient(path="./chroma_db")

# ---------- Agent ----------
agentic_retrieval = create_agent(
    model=llm,
    tools=[chroma_retrieval],
    system_prompt=(
        "You are an Agentic Retrieval system. "
        "You MUST use the chroma_retrieval tool "
        "before answering any question about a document."
    ),
)

st.header("Agentic Retrieval System")

# ---------- Upload PDF ----------
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:

    # ✅ Detect new PDF upload
    if st.session_state.get("last_pdf_name") != pdf_file.name:
        st.session_state["last_pdf_name"] = pdf_file.name

        # 🧹 Clear old collection ONCE
        try:
            client.delete_collection("mycollection")
        except Exception:
            pass

        collection = client.get_or_create_collection("mycollection")

        # Save temp PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf_file.read())
            pdf_path = tmp.name

        # Load & split
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100
        )
        chunks = splitter.split_documents(docs)

        # Index PDF
        texts = [c.page_content for c in chunks]
        metadatas = [c.metadata for c in chunks]
        ids = [f"chunk_{i}" for i in range(len(texts))]
        embeddings = [embeddings_model.embed_query(t) for t in texts]

        collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids,
            embeddings=embeddings
        )

        st.success("✅ New PDF indexed (old data cleared)")

    # ---------- Ask Question ----------
    user_question = st.text_input("Enter your question about the document:")

    if user_question:
        response = agentic_retrieval.invoke({
            "messages": [
                {"role": "user", "content": user_question}
            ]
        })

        answer = response["messages"][-1].content
        st.subheader("Answer:")
        st.write(answer)
