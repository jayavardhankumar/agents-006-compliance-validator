from app.models.audit_report import AuditReport


def create_report(
    ai_result,
    retrieved_rules
):

    return AuditReport(
        summary=ai_result.get(
            "summary",
            ""
        ),

        compliance_score=ai_result.get(
            "compliance_score",
            0
        ),

        risk_score=ai_result.get(
            "risk_score",
            0
        ),

        risk_level=ai_result.get(
            "risk_level",
            "UNKNOWN"
        ),

        risk_reasoning=ai_result.get(
            "risk_reasoning",
            ""
        ),

        retrieved_rules=retrieved_rules,

        violations=ai_result.get(
            "violations",
            []
        ),

        recommendations=ai_result.get(
            "recommendations",
            []
        ),

        confidence_score=ai_result.get(
            "confidence_score",
            0
        )
    )