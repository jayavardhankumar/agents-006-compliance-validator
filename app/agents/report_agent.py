from app.models.audit_report import AuditReport


def create_report(
    compliance_score,
    risk_score,
    risk_level,
    violations,
    recommendations,
    confidence_score
):

    return AuditReport(
        compliance_score=compliance_score,
        risk_score=risk_score,
        risk_level=risk_level,
        violations=violations,
        recommendations=recommendations,
        confidence_score=confidence_score
    )