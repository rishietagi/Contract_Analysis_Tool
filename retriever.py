
import json
import torch
from embedder import Embedder

class Retriever:
    def __init__(self, bucket_path):
        self.embedder = Embedder()

        with open(bucket_path, "r") as f:
            self.buckets = json.load(f)

        self.bucket_texts = [
            b["bucket_name"] + " " + " ".join(b["risk_patterns"])
            for b in self.buckets
        ]

        self.bucket_embeddings = self.embedder.embed(self.bucket_texts)

    def retrieve(self, clause, top_k=3):
        clause_emb = self.embedder.embed(clause)

        scores = torch.nn.functional.cosine_similarity(
            clause_emb, self.bucket_embeddings
        )

        top_indices = torch.topk(scores, k=top_k).indices.tolist()

        return [self.buckets[i] for i in top_indices]