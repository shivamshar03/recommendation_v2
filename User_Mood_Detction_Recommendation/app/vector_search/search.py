# vector_search/search.py

import numpy as np
from .indexer import FAISSIndexer

class FAISSSearcher:
    def __init__(self, indexer: FAISSIndexer, top_k: int = 5):
        self.indexer = indexer
        self.top_k = top_k

    def search(self, query_vector):
        if not self.indexer.index.is_trained or self.indexer.index.ntotal == 0:
            raise ValueError("FAISS index is empty or not trained.")

        query_vector = np.array([query_vector]).astype('float32')
        indices, distances = self.indexer.index.search(query_vector,None, self.top_k,None, None)

        results = []
        for idx, distance in zip(indices[0], distances[0]):
            metadata_id = self.indexer.get_metadata(idx)
            results.append({"metadata_id": metadata_id, "distance": distance})
        return results
