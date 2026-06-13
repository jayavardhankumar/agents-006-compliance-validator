from services.document_loader import read_file


def get_rules():

    rules = read_file(
        "data/rules/insurance_compliance_rules.txt"
    )

    return rules