# vector_search/indexer.py

import faiss
import numpy as np
import os
import pickle

class FAISSIndexer:
    def __init__(self, dim: int, index_path: str = "faiss.index", id_map_path: str = "id_map.pkl"):
        self.dim = dim
        self.index_path = index_path
        self.id_map_path = id_map_path
        self.index = faiss.IndexFlatL2(dim)  # L2 distance for similarity
        self.id_map = {}  # id -> metadata

        # For testing, always start fresh (do not load old index)
        # if os.path.exists(self.index_path) and os.path.exists(self.id_map_path):
        #     self.load_index()

    def build_index(self, vectors: np.ndarray, ids: list):
        vectors_np = np.array(vectors, dtype='float32')
        if vectors_np.size == 0:
            raise ValueError("Input vectors array is empty.")
        self.index.add(vectors_np,None)
        self.id_map = {i: ids[i] for i in range(len(ids))}
        print("FAISS id_map after build:", self.id_map)  # Debug print
        self.save_index()

    def add_vector(self, vector: np.ndarray, metadata_id):
        vector_np = np.array(vector, dtype='float32').reshape(1, -1)
        self.index.add(vector_np,None)
        self.id_map[len(self.id_map)] = metadata_id
        self.save_index()

    def save_index(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.id_map_path, 'wb') as f:
            pickle.dump(self.id_map, f)

    def load_index(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.id_map_path, 'rb') as f:
            self.id_map = pickle.load(f)

    def get_metadata(self, idx):
        return self.id_map.get(idx)
