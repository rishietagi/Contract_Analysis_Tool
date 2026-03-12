from llm import call_llm


def summarize_chunk(chunk, previous_context=""):

    prompt = f"""
You are a legal contract assistant.

You are reading the contract sequentially.

Previous extracted context from earlier clauses:
{previous_context}

Now extract important factual information from the next section.

Focus ONLY on:
- obligations
- deliverables
- payments
- deadlines
- responsibilities
- risks

Rules:
- Do NOT interpret
- Do NOT speculate
- Do NOT add information
- Keep bullet points concise

Contract text:
{chunk}
"""

    response = call_llm(prompt)

    print(response)

    return response


def summarize_with_context(chunks):

    summaries = []
    rolling_context = ""

    for chunk in chunks:

        summary = summarize_chunk(chunk, rolling_context)

        summaries.append(summary)

        # keep only recent context
        rolling_context = (rolling_context + "\n\n" + summary)[-2000:]

    return summaries


def deduplicate_summaries(summaries):

    seen = set()
    unique = []

    for summary in summaries:

        cleaned = summary.strip()

        if cleaned not in seen:
            unique.append(summary)
            seen.add(cleaned)

    return unique


def batch_reduce(summaries, batch_size=5):

    summaries = deduplicate_summaries(summaries)

    reduced = []

    for i in range(0, len(summaries), batch_size):

        batch = summaries[i:i + batch_size]

        batch_text = "\n\n".join(batch)

        prompt = f"""
You are combining contract notes extracted from multiple sections.

Tasks:
- Preserve ALL obligations
- Preserve payment terms
- Preserve deadlines
- Remove duplicate statements
- Merge similar points

Do NOT lose important contract details.

Notes:
{batch_text}
"""

        reduced.append(call_llm(prompt))

    return reduced