import re

def parse_contract(text):
    pattern = r"(?:\n|^)\s*(\d+)[\.\)]?\s*([^\n:\-]+?)\s*[:\-]\s*(.*?)(?=\n\d+[\.\)]|\Z)"

    matches = re.findall(pattern, text, re.DOTALL)

    clauses = []
    for num, title, body in matches:
        clauses.append({
            "id": num.strip(),
            "title": title.strip(),
            "text": body.strip()
        })

    return clauses