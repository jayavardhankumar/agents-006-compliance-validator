from agents.document_agent import extract_document
from agents.rule_agent import get_rules

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

    rules = get_rules()

    prompt = build_compliance_prompt(
        rules,
        document
    )

    response = await audit_document(
        prompt
    )

    return response