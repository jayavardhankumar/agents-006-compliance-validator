from app.rag.retriever import retrieve_rules

results = retrieve_rules(
    "insurance claim above 100000"
)

print(results)