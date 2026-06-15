from pydantic import BaseModel


class AuditReport(BaseModel):

    summary: str

    compliance_score: int

    risk_score: int

    risk_level: str

    risk_reasoning: str

    retrieved_rules: list[str]

    violations: list[str]

    recommendations: list[str]

    confidence_score: int