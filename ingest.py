import os
import glob
from dotenv import load_dotenv
from openai import OpenAI
import chromadb

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="client_blog")

EMBEDDING_MODEL = "text-embedding-3-small"


def get_embedding(text):
    response = openai_client.embeddings.create(model=EMBEDDING_MODEL, input=text)
    return response.data[0].embedding


def chunk_text(text, min_chunk_length=100):
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    chunks = [chunk for chunk in chunks if len(chunk) >= min_chunk_length]
    return chunks


def parse_frontmatter(content):
    """
    Parse the frontmatter from a markdown file.
    Frontmatter is the block between the two --- lines at the top of the file.
    Returns a dict of frontmatter fields and the body text separately.
    """
    frontmatter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, _, value = line.partition(":")
                    frontmatter[key.strip()] = value.strip()
            body = parts[2].strip()

    return frontmatter, body


def ingest_articles():
    print("\n--- Ingesting Client blog articles ---")

    article_files = glob.glob("data/articles/**/*.md", recursive=True)

    if not article_files:
        print("[WARN] No article files found in data/articles/")
        return

    for filepath in article_files:
        filename = os.path.basename(filepath)
        slug = filename.replace(".md", "")

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        title = frontmatter.get("title", slug)
        url = frontmatter.get("url", "")

        chunks = chunk_text(body)
        print(f"  {title}: {len(chunks)} chunk(s)")

        for i, chunk in enumerate(chunks):
            chunk_id = f"article-{slug}-chunk-{i}"
            embedding = get_embedding(chunk)

            collection.add(
                ids=[chunk_id],
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{
                    "source": "article",
                    "slug": slug,
                    "title": title,
                    "url": url,
                }]
            )

    print(f"\nIngestion complete. {collection.count()} chunks stored in ChromaDB.")


if __name__ == "__main__":
    print("Starting ingestion...")
    print(f"Embedding model: {EMBEDDING_MODEL}")
    ingest_articles()