import asyncio

from services.document_loader import read_file
from services.prompt_builder import (
    build_compliance_prompt
)

from agents.llm_compliance_agent import (
    audit_document
)


async def main():

    rules = read_file(
        "data/rules/insurance_compliance_rules.txt"
    )

    document = read_file(
        "data/sample_documents/sample_claim.txt"
    )

    prompt = build_compliance_prompt(
        rules,
        document
    )

    response = await audit_document(
        prompt
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())