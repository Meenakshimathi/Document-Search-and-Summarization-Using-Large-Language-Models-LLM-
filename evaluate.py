from rouge_score import rouge_scorer
from summarize import summarize

reference = "FAISS enables efficient vector similarity search."
generated = summarize("What is FAISS?", "short")

scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
scores = scorer.score(reference, generated)

print(scores)
