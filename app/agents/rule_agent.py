def detect_violations(document):

    violations = []

    if "Customer Signature" not in document:
        violations.append(
            "Missing Customer Signature"
        )

    if (
        "Claim Amount" in document
        and "150000" in document
        and "Manager Approval" not in document
    ):
        violations.append(
            "Missing Manager Approval"
        )

    if "Customer ID" not in document:
        violations.append(
            "Missing Customer ID"
        )

    return violations