def build_compliance_prompt(rules, document):

    prompt = f"""
You are an expert insurance compliance auditor.

Review the document against the compliance rules.

Compliance Rules:
{rules}

Document:
{document}

Tasks:
1. Calculate compliance score.
2. Identify violations.
3. Explain each violation.
4. Give recommendations.
5. Provide confidence score.

Return the response in a structured format.
"""

    return prompt