import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("demo")

collection.add(
    documents=[
        "AI is changing the world",
        "Python is easy to learn",
        "ChromaDB stores embeddings"
    ],
    ids=["1", "2", "3"]
)

print("document saved")

results = collection.query(
    query_texts=["What is Ai?"],
    n_results=2
) 

print("Search result:", results["documents"])
