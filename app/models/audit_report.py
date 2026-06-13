from dataclasses import dataclass


@dataclass
class AuditReport:

    compliance_score: int

    risk_score: int

    risk_level: str

    violations: list

    recommendations: list

    confidence_score: int