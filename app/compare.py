from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_similarity(resume_emb, role_emb):
    try:
        # Convert both to numpy arrays and reshape
        vec1 = np.array(resume_emb).reshape(1, -1)
        vec2 = np.array(role_emb).reshape(1, -1)

        similarity = cosine_similarity(vec1, vec2)[0][0]
        return round(similarity * 100, 2)  # Return as percentage
    except Exception as e:
        print(f"Similarity computation error: {e}")
        return 0.0
