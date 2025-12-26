from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings

llm=init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="openai",
    base_url="http://10.161.130.93:1234/v1",
    api_key="lm_studio"
)
embeddings_model=init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5-embedding",
    provider="openai",
    base_url="http://10.161.130.93:1234/v1",
    api_key="lm_studio",
    check_embedding_ctx_length=False
)
