from app.rag.vector_store import collection

rules = [
    "Customer ID must be present",
    "Policy Number must be present",
    "Claim Date must be present",
    "Customer Signature must be present",
    "Claims above 100000 require Manager Approval",
    "Supporting Documents must be attached",
    "Claim Amount must be clearly mentioned"
]

for idx, rule in enumerate(rules):

    collection.add(
        ids=[f"rule_{idx}"],
        documents=[rule]
    )

print(f"Loaded {len(rules)} rules")