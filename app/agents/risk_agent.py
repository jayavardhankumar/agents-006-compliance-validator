def calculate_risk(document):

    score = 0

    text = document.lower()

    if "signature" not in text:
        score += 30

    if "manager approval" not in text:
        score += 30

    if "supporting document" not in text:
        score += 20

    if score >= 60:
        level = "HIGH"

    elif score >= 30:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "risk_score": score,
        "risk_level": level
    }