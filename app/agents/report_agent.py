from app.models.audit_report import AuditReport


def create_report(
    retrieved_rules,
    risk_result,
    violations
):

    compliance_score = max(
        0,
        100 - (len(violations) * 20)
    )

    return AuditReport(
        compliance_score=compliance_score,
        risk_score=risk_result["risk_score"],
        risk_level=risk_result["risk_level"],
        retrieved_rules=retrieved_rules,
        violations=violations,
        recommendations=[
            "Fix all violations",
            "Re-run compliance audit"
        ],
        confidence_score=85
    )