from pathlib import Path


def load_rules():

    with open(
        "data/rules/insurance_compliance_rules.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def load_document():

    with open(
        "data/sample_documents/sample_claim.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()