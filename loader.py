import os
import pdfplumber


def load_contract(path):

    ext = os.path.splitext(path)[1].lower()

    if ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    elif ext == ".pdf":

        text = []

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text.append(page_text)

        return "\n".join(text)

    else:
        raise ValueError("Unsupported file type")