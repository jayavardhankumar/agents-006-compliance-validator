from app.agents.document_agent import (
    extract_document
)

from app.agents.llm_compliance_agent import (
    audit_document
)

from app.agents.report_agent import (
    create_report
)

from app.rag.retriever import (
    retrieve_rules
)

from app.services.prompt_builder import (
    build_compliance_prompt
)

from app.services.json_parser import (
    parse_ai_response
)


async def run_compliance_audit(
    document_path
):

    print(
        "STEP 1: Loading document"
    )

    document = extract_document(
        document_path
    )

    print(
        "STEP 2: Retrieving rules"
    )

    retrieved_rules = retrieve_rules(
        document
    )

    print(
        "STEP 3: Building prompt"
    )

    prompt = build_compliance_prompt(
        retrieved_rules,
        document
    )

    print(
        "STEP 4: Running AI Compliance Agent"
    )

    ai_response = await audit_document(
        prompt
    )

    print(
        "STEP 5: Parsing AI Response"
    )

    ai_result = parse_ai_response(
        ai_response
    )

    print(
        "STEP 6: Creating Report"
    )

    report = create_report(
        ai_result,
        retrieved_rules
    )

    return report.model_dump()