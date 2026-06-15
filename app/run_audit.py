import asyncio

from app.agents.compliance_orchestrator import (
    run_compliance_audit
)

from app.services.report_generator import (
    generate_report
)


async def main():

    report = await run_compliance_audit(
        "data/sample_documents/sample_claim.txt"
    )

    formatted_report = generate_report(
        report
    )

    print(
        formatted_report
    )


if __name__ == "__main__":
    asyncio.run(main())