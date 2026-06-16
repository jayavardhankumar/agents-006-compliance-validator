def make_decision(
    compliance_score,
    risk_score
):

    if compliance_score >= 85 and risk_score <= 30:

        return "APPROVE"

    if risk_score >= 70:

        return "MANUAL_REVIEW"

    return "REVIEW_REQUIRED"