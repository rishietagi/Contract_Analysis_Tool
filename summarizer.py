from llm import call_llm


def summarize_chunk(chunk):

    prompt = f"""
You are a legal contract assistant.

Read the contract text and extract important factual information.

Focus only on:
- obligations
- deliverables
- payments
- deadlines
- responsibilities
- risks

Do NOT interpret.
Do not speculate.
Do NOT add information.

Contract Text:
{chunk}
"""
    print(call_llm(prompt))
    return call_llm(prompt)



def batch_reduce(summaries, batch_size=5):

    reduced = []

    for i in range(0, len(summaries), batch_size):

        batch = summaries[i:i+batch_size]

        batch_text = "\n\n".join(batch)

        prompt = f"""
Combine the following contract notes.

Preserve ALL important details.
Remove repetition.
Do not lose obligations or payment terms.

Notes:
{batch_text}
"""

        reduced.append(call_llm(prompt))

    return reduced

