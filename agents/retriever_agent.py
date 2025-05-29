# agents/retriever_agent.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)  # 384 = embedding size for MiniLM
        self.documents = []

    def ingest(self, docs):
        """
        Ingests a list of documents (strings).
        """
        self.documents = docs
        embeddings = self.model.encode(docs)
        self.index.add(np.array(embeddings))

    def retrieve(self, query, k=3):
        """
        Retrieves top-k similar documents to the query.
        """
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec), k)
        return [self.documents[i] for i in I[0]]
