from tools.rule_checker import (
    load_document,
    check_compliance
)

document = load_document()

violations = check_compliance(document)

print("\nCompliance Audit Report\n")

if violations:
    print("Violations Found:\n")

    for v in violations:
        print("-", v)

else:
    print("Document is compliant.")