from app.agents.document_agent import extract_document
from app.agents.rule_agent import detect_violations
from app.agents.risk_agent import calculate_risk
from app.agents.report_agent import create_report

from app.rag.retriever import retrieve_rules


async def run_compliance_audit(document_path):

    print("STEP 1: Loading document")

    document = extract_document(
        document_path
    )

    print("STEP 2: Retrieving rules")

    retrieved_rules = retrieve_rules(
        document
    )

    print("STEP 3: Calculating risk")

    risk_result = calculate_risk(
        document
    )

    print("STEP 4: Detecting violations")

    violations = detect_violations(
        document
    )

    print("STEP 5: Creating report")

    report = create_report(
        retrieved_rules,
        risk_result,
        violations
    )

    return report.model_dump()