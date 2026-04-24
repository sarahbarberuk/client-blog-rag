import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="client_blog")

# ---- Total chunk count ----
print("=== Total chunks in ChromaDB ===")
print(f"{collection.count()} chunks stored")
print()

# ---- Chunks per source ----
print("=== Chunks by source ===")
results = collection.get(where={"source": "article"})
print(f"  article: {len(results['ids'])} chunks")
print()

# ---- Look at a sample chunk ----
print("=== Sample chunk ===")
results = collection.get(
    where={"source": "article"},
    limit=1,
    include=["documents", "metadatas"]
)

print(f"Title: {results['metadatas'][0]['title']}")
print(f"URL: {results['metadatas'][0]['url']}")
print(f"Text (first 300 characters):")
print(f"  {results['documents'][0][:300]}...")