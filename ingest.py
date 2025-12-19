import faiss
import numpy as np
from embeddings import get_embedding

# ----------------------------
# Raw documents (corpus)
# ----------------------------
documents = [
    "Artificial Intelligence enables machines to mimic human intelligence.",
    "FAISS enables fast similarity search over vector embeddings.",
    "Retrieval Augmented Generation combines search with generation.",
    "Large Language Models are trained on massive datasets.",

    # ---- Enterprise Case Study ----
    """
    Perkins & Will is a globally recognized leader in the architecture and design industry,
    known for its commitment to creativity, innovation, and excellence. The firm operates
    across multiple continents, employing a diverse and talented workforce dedicated to
    delivering high-quality design solutions.
    """,

    """
    Despite this success, the firm faced a challenge with its employee management system.
    There was no centralized location to view employee details and their corresponding projects.
    Users had to navigate between different platforms—first going to UKG to find employee IDs,
    then switching to Deltek to locate project information.
    """,

    """
    To address this, a unified portal was developed that integrated employee data with their
    projects and pursuits, streamlining the process and improving overall efficiency.
    """,

    """
    The People app is designed to capture all essential details about an individual within
    a company. It includes basic information like name, email address, and job role, as well
    as digital portfolios, recent activities, active projects, and connections.
    """,

    """
    The layout of the People app is simple and intuitive, with clearly defined sections such
    as Information, Professional, Activities, Connections, Pipeline, and Projects, enabling
    users to quickly navigate and access relevant information.
    """,

    """
    One of the key features is the ability to see which projects an individual is working on
    directly from their profile. This eliminates the need to visit the pipeline app and
    manually search for projects.
    """,

    """
    The profile is always updated in real-time, ensuring that whether a person is actively
    engaged in a project or has moved on, the information remains accurate.
    """,

    """
    The Activities section tracks tasks assigned to individuals in the pipeline app,
    showing which tasks have been completed and which remain pending.
    """,

    """
    The Connections section allows users to bookmark important people outside the organization.
    These bookmarked contacts automatically appear in the People app, creating a unified
    view of professional relationships.
    """
]

# ----------------------------
# Generate embeddings
# ----------------------------
vectors = np.vstack([get_embedding(doc) for doc in documents])

# ----------------------------
# Build FAISS index
# ----------------------------
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(vectors)

# ----------------------------
# Persist index and documents
# ----------------------------
faiss.write_index(index, "faiss.index")
np.save("docs.npy", np.array(documents, dtype=object))

print(f"FAISS index created with {len(documents)} document chunks")
