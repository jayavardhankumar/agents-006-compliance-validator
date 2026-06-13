from agents.document_agent import extract_document

from app.rag.retriever import retrieve_rules

from services.prompt_builder import (
    build_compliance_prompt
)

from agents.llm_compliance_agent import (
    audit_document
)


async def run_compliance_audit(
    document_path
):

    document = extract_document(
        document_path
    )

    retrieved_rules = retrieve_rules(
        document
    )

    prompt = build_compliance_prompt(
        retrieved_rules,
        document
    )

    response = await audit_document(
        prompt
    )

    return response