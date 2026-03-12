from loader import load_contract
from chunking import chunk_clauses
from summarizer import summarize_with_context, batch_reduce
from review import generate_contract_review
from parser import parse_review


def run_pipeline():

    # 1 Load contract
    contract_text = load_contract("contract.pdf")

    print("Contract loaded:", len(contract_text))

    # 2 Chunk
    chunks = chunk_clauses(contract_text)
    print("Chunks:", len(chunks))

    # 3 First pass (rolling context summarization)
    chunk_summaries = summarize_with_context(chunks)

    print("Chunk summaries done")

    # 4 Reduction passes
    level_2 = batch_reduce(chunk_summaries)
    level_3 = batch_reduce(level_2)

    combined_notes = "\n\n".join(level_3)

    # 5 Final review
    review_context = combined_notes + "\n\nRecent Clause Evidence:\n\n" + "\n\n".join(chunk_summaries[-3:])

    final_review = generate_contract_review(review_context)

    print(final_review)

    df = parse_review(final_review)

    df.to_csv("contract_review.csv", index=False)

    print("Review saved to contract_review.csv")


if __name__ == "__main__":
    run_pipeline()