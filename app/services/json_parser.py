import json


def parse_ai_response(response):

    try:
        return json.loads(response)

    except Exception as e:

        print(
            f"JSON Parse Error: {e}"
        )

        return {
            "summary": "Failed to parse AI response",
            "compliance_score": 0,
            "risk_score": 0,
            "risk_level": "UNKNOWN",
            "risk_reasoning": "",
            "violations": [],
            "recommendations": [],
            "confidence_score": 0
        }