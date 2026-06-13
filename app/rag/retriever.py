from app.rag.vector_store import collection


def retrieve_rules(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results["documents"][0]