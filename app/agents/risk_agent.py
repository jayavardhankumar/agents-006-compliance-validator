def calculate_risk(violations):

    count = len(violations)

    if count == 0:
        return "LOW"

    if count <= 2:
        return "MEDIUM"

    return "HIGH"
