import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import init_embeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import tempfile


# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"


# ------------------ Pages ------------------
def home_page():
    st.header("AI-Enabled Resume Shortlisting System")
    st.subheader("Powered by Generative AI & RAG")


def upload_resume():
    st.header("Upload Resume")

    embed_model = init_embeddings(
        model="text-embedding-nomic-embed-text-v1.5-embedding",
        provider="openai",
        base_url="http://127.0.0.1:1234/v1",
        api_key="none",
        check_embedding_ctx_length=False
    )

    resume_file = st.file_uploader("Browse PDF", type="pdf")

    if resume_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        documents = []
        for page in pages:
            chunks = splitter.split_text(page.page_content)
            for chunk in chunks:
                documents.append(
                    Document(
                        page_content=chunk,
                        metadata={"source": resume_file.name}
                    )
                )

        vectordb = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embed_model
        )

        vectordb.add_documents(documents)
        vectordb.persist()

        st.success(f"Resume '{resume_file.name}' uploaded and indexed successfully!")


def shortlist_resumes():
    st.header("Shortlist Resumes for Job Description")

    job_desc = st.text_area(
        "Enter Job Description",
        height=200,
        placeholder="e.g. Python developer with Django, REST APIs, SQL"
    )

    top_k = st.number_input(
        "Number of candidates to shortlist",
        min_value=1,
        max_value=10,
        value=3
    )

    if st.button("Shortlist Candidates"):
        if not job_desc.strip():
            st.warning("Please enter a job description")
            return

        embed_model = init_embeddings(
            model="text-embedding-nomic-embed-text-v1.5-embedding",
            provider="openai",
            base_url="http://127.0.0.1:1234/v1",
            api_key="none",
            check_embedding_ctx_length=False
        )

        vectordb = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embed_model
        )

        results = vectordb.similarity_search_with_score(job_desc, k=top_k)

        if not results:
            st.info("No matching resumes found")
            return

        st.subheader("Shortlisted Candidates")

        seen = set()
        rank = 1

        for doc, score in results:
            source = doc.metadata.get("source", "Unknown")

            if source in seen:
                continue

            seen.add(source)

            st.markdown(
                f"""
                **Rank {rank}**
                - **Resume:** {source}
                - **Relevance Score:** `{round(score, 4)}`
                - **Matched Content:**  
                  {doc.page_content[:300]}...
                """
            )
            st.divider()
            rank += 1


def list_resumes():
    st.header("List All Resumes")

    embed_model = init_embeddings(
        model="text-embedding-nomic-embed-text-v1.5-embedding",
        provider="openai",
        base_url="http://127.0.0.1:1234/v1",
        api_key="none",
        check_embedding_ctx_length=False
    )

    vectordb = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embed_model
    )

    data = vectordb.get(include=["metadatas"])

    if not data or not data["metadatas"]:
        st.info("No resumes found")
        return

    resume_names = sorted(
        set(meta["source"] for meta in data["metadatas"])
    )

    st.subheader(f"Total Resumes: {len(resume_names)}")

    for i, name in enumerate(resume_names, start=1):
        st.write(f"{i}. {name}")


# ------------------ Sidebar ------------------
with st.sidebar:
    st.subheader("Select Options")

    if st.button("Upload Resume (PDF)", width="stretch"):
        st.session_state.page = "Upload Resume (PDF)"

    if st.button("Shortlist Resumes", width="stretch"):
        st.session_state.page = "Shortlist Resumes"

    if st.button("Update Resume", width="stretch"):
        st.session_state.page = "Update Resume"

    if st.button("Delete Resume", width="stretch"):
        st.session_state.page = "Delete Resume"

    if st.button("List All Resumes", width="stretch"):
        st.session_state.page = "List All Resumes"


# ------------------ Page Routing ------------------
if st.session_state.page == "Home":
    home_page()

elif st.session_state.page == "Upload Resume (PDF)":
    upload_resume()

elif st.session_state.page == "Shortlist Resumes":
    shortlist_resumes()

elif st.session_state.page == "List All Resumes":
    list_resumes()
