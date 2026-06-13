from services.document_loader import read_file
from services.prompt_builder import build_compliance_prompt


def main():

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

    print(prompt)


if __name__ == "__main__":
    main()