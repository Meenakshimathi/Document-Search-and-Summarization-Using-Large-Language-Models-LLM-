from together import Together
from search import search

client = Together(api_key="tgp_v1_w5LayAUjhjUS9YJRbXpqrldJJiwUT7wOctEx4ll26Vo")

def summarize(query, length="short"):
    context = "\n".join(search(query))

    prompt = f"Summarize the following in a {length} way:\n{context}"

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
