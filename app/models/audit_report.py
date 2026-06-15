from pydantic import BaseModel


class AuditReport(BaseModel):

    compliance_score: int

    risk_score: int

    risk_level: str

    retrieved_rules: list[str]

    violations: list[str]

    recommendations: list[str]

    confidence_score: int