import logging

logger = logging.getLogger(__name__)

try:
    from sentence_transformers import SentenceTransformer, util
    import torch
    # Load a pre-trained sentence transformer model
    # all-MiniLM-L6-v2 is small and fast, good for production use without GPUs
    model = SentenceTransformer('all-MiniLM-L6-v2')
    AI_AVAILABLE = True
except Exception as e:
    logger.warning(f"Failed to load sentence_transformers: {e}. Semantic scoring will be mocked.")
    model = None
    AI_AVAILABLE = False

def calculate_semantic_similarity(student_answer, model_answer):
    """
    Calculates the cosine similarity between the student's answer and the model answer.
    Returns a score from 0 to 100.
    """
    if not student_answer.strip() or not model_answer.strip():
        return 0.0

    if not AI_AVAILABLE:
        # Fallback dummy score if AI engine couldn't load (e.g. missing MSVC++ redist)
        return 75.0

    # Compute embeddings
    embeddings1 = model.encode(student_answer, convert_to_tensor=True)
    embeddings2 = model.encode(model_answer, convert_to_tensor=True)

    # Compute cosine similarity
    cosine_scores = util.cos_sim(embeddings1, embeddings2)
    
    # Extract scalar value, clip negative values to 0, and scale to 0-100
    score = cosine_scores.item()
    if score < 0:
        score = 0.0
    
    return score * 100.0
