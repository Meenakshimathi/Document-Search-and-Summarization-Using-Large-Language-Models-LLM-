import os
import numpy as np
from together import Together

os.environ["TOGETHER_NO_BANNER"] = "1"

client = Together(api_key="YOUR_API_KEY")

def get_embedding(text: str) -> np.ndarray:
    response = client.embeddings.create(
        model="togethercomputer/m2-bert-80M-8k-retrieval",
        input=text
    )
    return np.array(response.data[0].embedding, dtype="float32")
