def generate_report(report):

    output = f"""
AI COMPLIANCE AUDIT REPORT
==================================================

Compliance Score : {report['compliance_score']}%

Risk Score       : {report['risk_score']}

Risk Level       : {report['risk_level']}

--------------------------------------------------
RULES CHECKED
--------------------------------------------------
"""

    for rule in report["retrieved_rules"]:
        output += f"\n✓ {rule}"

    output += """

--------------------------------------------------
VIOLATIONS
--------------------------------------------------
"""

    for violation in report["violations"]:
        output += f"\n✗ {violation}"

    output += """

--------------------------------------------------
RECOMMENDATIONS
--------------------------------------------------
"""

    for recommendation in report["recommendations"]:
        output += f"\n• {recommendation}"

    output += f"""

--------------------------------------------------

Confidence Score : {report['confidence_score']}%

==================================================
"""

    with open(
        "audit_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(output)

    return output