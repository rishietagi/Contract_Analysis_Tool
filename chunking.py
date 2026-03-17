import re


def split_into_clauses(text):

    """
    Split contract text using common clause patterns
    like:
    1.
    1.1
    Article 1
    Section 2
    """

    pattern = r"\n(?=\s*(?:Article|Section|\d+\.\d+|\d+\.)\s)"

    clauses = re.split(pattern, text)

    return [c.strip() for c in clauses if c.strip()]


def chunk_clauses(text, max_chars=2000):

    clauses = split_into_clauses(text)

    chunks = []
    current_chunk = ""

    for clause in clauses:

        if len(current_chunk) + len(clause) < max_chars:
            current_chunk += "\n\n" + clause

        else:
            chunks.append(current_chunk.strip())
            current_chunk = clause

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks