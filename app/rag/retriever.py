from app.rag.vector_store import collection


RULEBOOK_PATH = (
    "data/rules/insurance_compliance_rules.txt"
)

def load_full_rulebook():

    rules = []

    with open(
        RULEBOOK_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith(
                "Insurance Claim Compliance Rules"
            ):
                continue

            if line.startswith(
                "Rule "
            ):
                continue

            rules.append(line)

    return rules

def retrieve_rules(query):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    retrieved_rules = (
        results["documents"][0]
        if results["documents"]
        else []
    )

    full_rulebook = (
        load_full_rulebook()
    )

    merged_rules = list(
        dict.fromkeys(
            retrieved_rules
            + full_rulebook
        )
    )

    return merged_rules