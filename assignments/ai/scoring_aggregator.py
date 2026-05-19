from .nlp_engine import calculate_keyword_score
from .semantic_scorer import calculate_semantic_similarity
from .grammar_checker import check_grammar

def evaluate_submission(student_text, model_answer, keywords, rubric):
    """
    Evaluates the student submission using the AI engines and rubric.
    Returns a dictionary of scores and feedback.
    """
    
    # 1. Semantic Similarity
    semantic_score = calculate_semantic_similarity(student_text, model_answer)
    
    # 2. Keyword Coverage
    keyword_score = calculate_keyword_score(student_text, keywords)
    
    # 3. Grammar Checking
    grammar_score, grammar_feedback = check_grammar(student_text)
    
    # 4. Aggregation
    final_score = (
        (semantic_score * rubric.semantic_weight) +
        (grammar_score * rubric.grammar_weight) +
        (keyword_score * rubric.keyword_weight)
    )
    
    # Cap final score at 100
    if final_score > 100.0:
        final_score = 100.0
        
    feedback = {
        "semantic": "Your answer is highly relevant to the model answer." if semantic_score > 80 else "Your answer could align more closely with the expected core concepts.",
        "keywords": f"You covered {keyword_score:.1f}% of the required keywords.",
        "grammar_suggestions": grammar_feedback
    }
    
    return {
        "semantic_score": semantic_score,
        "grammar_score": grammar_score,
        "keyword_score": keyword_score,
        "final_score": final_score,
        "feedback_json": feedback
    }
