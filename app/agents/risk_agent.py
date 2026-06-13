def calculate_risk(
    violations,
    claim_amount=0
):

    score = 0

    score += len(violations) * 20

    if claim_amount > 100000:
        score += 20

    if score <= 20:
        risk = "LOW"

    elif score <= 50:
        risk = "MEDIUM"

    elif score <= 80:
        risk = "HIGH"

    else:
        risk = "CRITICAL"

    return {
        "risk_level": risk,
        "risk_score": min(score, 100)
    }