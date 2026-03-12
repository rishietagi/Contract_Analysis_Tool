import re
import pandas as pd


def parse_review(text):

    rows = []

    pattern = r"\n?(\d+)\.\s([^\n:]+):\s*(Covered|Not Covered|Partially Covered)"

    matches = list(re.finditer(pattern, text))

    for i, match in enumerate(matches):

        clause_number = match.group(1)
        clause_title = match.group(2).strip()
        status = match.group(3).strip()

        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        section_text = text[start:end]

        remarks_match = re.search(r"Remarks:\s*(.*)", section_text)

        remarks = remarks_match.group(1).strip() if remarks_match else ""

        rows.append({
            "Clause Name": clause_title,
            "Status": status,
            "Impact": "",
            "Remarks": remarks
        })

    return pd.DataFrame(rows)
    