"""Response formatting helpers for the LangChain RAG API."""

CHAIN_EXPRESSION = "ChatPromptTemplate | ChatOllama | StrOutputParser"

COMPONENTS = {
    "vector_store": "Chroma",
    "retrieval_method": "similarity_search_with_score",
    "prompt_template": "ChatPromptTemplate",
    "chat_model": "ChatOllama",
    "output_parser": "StrOutputParser",
}

SCORE_TYPE = "Chroma distance; lower usually means closer in this lesson setup"

FALLBACK_ANSWER = (
    "I do not have enough approved runbook context to answer that reliably."
)


def format_sources(scored_documents):
    """Format retrieved documents as source metadata for the API response."""

    # TODO: Return a list of dictionaries.
    # Each dictionary should include source_id, title, category, section,
    # chunk_id, and distance.
    # Do not include full document text in the source list.
    sources = []
    seen_chunk_ids = set()

    for document, distance in scored_documents:
        metadata = document.metadata or {}
        chunk_id = metadata.get("chunk_id")

        if chunk_id in seen_chunk_ids:
            continue

        seen_chunk_ids.add(chunk_id)

        sources.append(
            {
                "source_id": metadata.get("source_id", "unknown"),
                "title": metadata.get("title", "Untitled"),
                "category": metadata.get("category", "Uncategorized"),
                "section": metadata.get("section", "Unspecified"),
                "chunk_id": chunk_id or "unknown",
                "distance": round(float(distance), 4),
            }
        )

    return sources


def format_langchain_debug(scored_documents, context, top_k, fallback):
    """Return LangChain debug metadata for inspectability."""

    # TODO: Return chain expression, component names, retrieved count,
    # retrieved chunk IDs, top_k, context length, fallback status, and score type.
    retrieved_chunk_ids = [
        document.metadata.get("chunk_id", "unknown")
        for document, _distance in scored_documents
    ]

    return {
        "chain_expression": "ChatPromptTemplate | ChatOllama | StrOutputParser",
        "components": {
            "vector_store": "Chroma",
            "retrieval_method": "similarity_search_with_score",
            "prompt_template": "ChatPromptTemplate",
            "chat_model": "ChatOllama",
            "output_parser": "StrOutputParser",
        },
        "retrieved_count": len(scored_documents),
        "retrieved_chunk_ids": retrieved_chunk_ids,
        "top_k": top_k,
        "context_characters": len(context or ""),
        "fallback": fallback,
        "score_type": "Chroma distance; lower usually means closer in this lesson setup",
        "models": {
            "embedding": "text-embedding-3-small",
            "generation": "ollama-model-name",
        },
    }


def format_success_response(answer, sources, debug):
    """Format a successful RAG response."""

    # TODO: Return a dictionary with answer, sources, and langchain.
    return {
        "answer": answer.strip(),
        "sources": sources,
        "langchain": debug,
    }


def format_fallback_response(debug):
    """Format a safe response when no usable context is available."""

    # TODO: Return a response with FALLBACK_ANSWER, empty sources, and debug.
    return {
        "answer": FALLBACK_ANSWER,
        "sources": [],
        "langchain": debug or {"fallback": True},
    }



def format_error_response(error, message):
    """Format an API error response."""

    # TODO: Return a dictionary with error and message.
    return {"error": error, "message": message}
