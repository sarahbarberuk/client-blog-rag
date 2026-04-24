# client-blog-rag

## Setup

1. Create .env file and copy .env.example into it. Add your keys.
2. Create a virtual environment, and activate it:

python -m venv venv
venv\Scripts\activate

install software needed:

pip install -r requirements.txt
playwright install chromium

## Scrape

SCrape data into data/articles:

`python scrape.py`

## Ingest

Ingest the data from data/article sinto the vector db

`python ingest.py`

## Checking the vector DB

Run this script to take a quick look at a sample of what is now in the vector DB. To check it worked, and for cuuriosity.

`python check_vectordb.py`

## Querying the vector DB

`python query.py`

Ask a question like:

What articles could I link to from a new article about RAG

## Try the FastAPI web front end

Start the web app
`uvicorn app:app --reload`

## Note to self

Check if all CTFL blog posts get scraped or just the "guides" ones?
Only 12 posts scraped? the see more button msut have changed.
