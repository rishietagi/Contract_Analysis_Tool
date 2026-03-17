import json
import pandas as pd


def parse_review(text):
    try:
        # Extract JSON safely
        start = text.find('[')
        end = text.rfind(']') + 1
        json_str = text[start:end]

        data = json.loads(json_str)

        rows = []

        for item in data:
            rows.append({
                "Section Number": item.get("section_number", ""),
                "Clause Name": item.get("section_name", ""),
                "Status": item.get("status", ""),
                "Impact": item.get("impact", ""),
                "Remarks": item.get("remarks", ""),
                "Evidence": item.get("evidence", "")
            })

        df = pd.DataFrame(rows)

        return df

    except Exception as e:
        print("❌ JSON parsing failed:", e)
        print("RAW OUTPUT:\n", text)
        return pd.DataFrame()