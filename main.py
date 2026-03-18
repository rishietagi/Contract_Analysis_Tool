from loader import load_contract
from chunking import chunk_clauses
from summarizer import summarize_with_context, batch_reduce
from review import generate_contract_review
from parser import parse_review

# 🔥 NEW IMPORTS (RAG)
from RAG_parser import parse_contract
from retriever import Retriever
from risk_LLM import analyze_clause
from score import compute_score

import json


def run_pipeline():

    # =======================
    # SUMMARIZER PIPELINE
    # =======================

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

    # =======================
    # RAG RISK PIPELINE
    # =======================

    print("\nStarting Risk Analysis...\n")

    # 1 Parse clauses
    clauses = parse_contract(contract_text)
    print("Clauses extracted:", len(clauses))

    # 2 Load retriever
    retriever = Retriever("buckets.JSON")

    risk_results = []

    # 3 Analyze each clause
    for clause in clauses:
        clause_text = clause["text"]

        retrieved = retriever.retrieve(clause_text)
        analysis = analyze_clause(clause_text, retrieved)

        # optional: attach clause info
        analysis["clause_id"] = clause.get("id", "")
        analysis["clause_title"] = clause.get("title", "")

        risk_results.append(analysis)

    # 4 Compute score
    risk_score = compute_score(risk_results)

    # 5 Save output
    final_output = {
        "risk_score": risk_score,
        "total_clauses": len(clauses),
        "risk_details": risk_results
    }

    with open("risk_analysis.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("\nRisk Analysis Completed")
    print("Risk Score:", risk_score)
    print("Saved to risk_analysis.json")


if __name__ == "__main__":
    run_pipeline()