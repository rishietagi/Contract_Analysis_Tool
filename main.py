from loader import load_contract
from chunking import chunk_text
from summarizer import summarize_chunk, batch_reduce
from review import generate_contract_review
from parser import parse_review


def run_pipeline():

    # 1 Load contract
    contract_text = load_contract("contract.pdf")

    print("Contract loaded:", len(contract_text))

    # 2 Chunk
    chunks = chunk_text(contract_text)

    print("Chunks:", len(chunks))

    # 3 First pass
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=4) as executor:
        chunk_summaries = list(executor.map(summarize_chunk, chunks))

    print("Chunk summaries done")

    # 4 Reduction passes
    level_2 = batch_reduce(chunk_summaries)
    level_3 = batch_reduce(level_2)

    combined_notes = "\n\n".join(level_3)

    # 5 Final review
    final_review = generate_contract_review(combined_notes)

    print(final_review)

    df = parse_review(final_review)

    df.to_csv("contract_review.csv", index=False)

    print("Review saved to contract_review.csv")


if __name__ == "__main__":
    run_pipeline()