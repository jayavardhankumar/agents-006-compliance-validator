import json
import os


HISTORY_FILE = "audit_history.json"


def save_audit(report):

    history = []

    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            try:
                history = json.load(file)

            except Exception:
                history = []

    history.append(report)

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )