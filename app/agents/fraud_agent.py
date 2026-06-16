def detect_fraud(
    document_text
):

    fraud_score = 0

    text = document_text.lower()

    # Suspicious keywords

    if "urgent payout" in text:
        fraud_score += 30

    if "cash only" in text:
        fraud_score += 20

    if "manual override" in text:
        fraud_score += 40

    if "immediate settlement" in text:
        fraud_score += 20

    if "expedite payment" in text:
        fraud_score += 20

    # Fraud level

    if fraud_score >= 70:

        fraud_risk = "HIGH"

    elif fraud_score >= 30:

        fraud_risk = "MEDIUM"

    else:

        fraud_risk = "LOW"

    return {
        "fraud_risk": fraud_risk,
        "fraud_score": fraud_score
    }