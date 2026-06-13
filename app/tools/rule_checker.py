from pathlib import Path


def load_rules():
    rules_path = Path("data/rules/insurance_compliance_rules.txt")

    with open(rules_path, "r", encoding="utf-8") as f:
        return f.read()


def load_document():
    document_path = Path(
        "data/sample_documents/sample_claim.txt"
    )

    with open(document_path, "r", encoding="utf-8") as f:
        return f.read()


def check_compliance(document_text):
    violations = []

    if "customer id" not in document_text.lower():
        violations.append("Missing Customer ID")

    if "policy number" not in document_text.lower():
        violations.append("Missing Policy Number")

    if "claim date" not in document_text.lower():
        violations.append("Missing Claim Date")

    if "signature" not in document_text.lower():
        violations.append("Missing Customer Signature")

    if "claim amount" in document_text.lower():
        try:
            amount_line = [
                line
                for line in document_text.splitlines()
                if "claim amount" in line.lower()
            ][0]

            amount = int(
                ''.join(filter(str.isdigit, amount_line))
            )

            if amount > 100000:
                if "manager approval" not in document_text.lower():
                    violations.append(
                        "Missing Manager Approval"
                    )

        except:
            pass

    return violations