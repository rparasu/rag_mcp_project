"""
========================================================
📚 RAG TOOL (VECTOR SEARCH USING PINECONE)
========================================================

WHAT THIS FILE DOES:
--------------------
Implements Retrieval-Augmented Generation (RAG).

FLOW:
-----
1. Convert user query → embedding (vector)
2. Search Pinecone vector database
3. Return most relevant results

WHY THIS MATTERS:
-----------------
LLMs alone:
❌ Don't know your custom data
❌ Can hallucinate

RAG solves this:
✔ Retrieves real data
✔ Improves accuracy
"""

import os
from openai import OpenAI
from pinecone import Pinecone

from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Initialize Pinecone client
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Name of your Pinecone index
INDEX_NAME = "city-rag-index"


def rag_search(query: str) -> str:
    """
    Perform semantic search.

    PARAMETERS:
    -----------
    query : str
        User query

    RETURNS:
    --------
    str
        Relevant context from database
    """

    # Connect to Pinecone index
    index = pc.Index(INDEX_NAME)

    # STEP 1: Convert query to embedding
    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    # STEP 2: Search Pinecone
    results = index.query(
        vector=embedding,
        top_k=2,
        include_metadata=True
    )

    # STEP 3: Extract text results
    matches = [
        match["metadata"]["text"]
        for match in results["matches"]
    ]

    # Return combined context
    return "\n".join(matches) if matches else "No relevant data found"