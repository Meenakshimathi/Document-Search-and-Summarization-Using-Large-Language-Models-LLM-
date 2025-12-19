import faiss
import numpy as np
from embeddings import get_embedding

index = faiss.read_index("faiss.index")
docs = np.load("docs.npy", allow_pickle=True)

def search(query, top_k=3):
    q_vec = get_embedding(query).reshape(1, -1)
    _, ids = index.search(q_vec, top_k)
    return [docs[i] for i in ids[0]]
