import asyncio

from agents.compliance_orchestrator import (
    run_compliance_audit
)


async def main():

    report = await run_compliance_audit(
        "data/sample_documents/sample_claim.txt"
    )

    print(report)


if __name__ == "__main__":
    asyncio.run(main())