import re
import logging

logger = logging.getLogger(__name__)

try:
    import spacy
    # Load English tokenizer, tagger, parser and NER
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        import spacy.cli
        spacy.cli.download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except Exception as e:
    logger.warning(f"Failed to load spacy: {e}. NLP functions will be mocked.")
    nlp = None
    SPACY_AVAILABLE = False

def preprocess_text(text):
    """
    Cleans and preprocesses the text for analysis.
    Lowercases, removes punctuation, and lemmatizes.
    """
    if not SPACY_AVAILABLE:
        return text.lower() # Fallback

    doc = nlp(text)
    cleaned = []
    for token in doc:
        if not token.is_punct and not token.is_space and not token.is_stop:
            cleaned.append(token.lemma_.lower())
    return " ".join(cleaned)

def extract_keywords(text):
    """
    Extracts key noun chunks and entities as potential keywords.
    """
    if not SPACY_AVAILABLE:
        return text.lower().split() # Fallback

    doc = nlp(text)
    keywords = set()
    for chunk in doc.noun_chunks:
        keywords.add(chunk.text.lower())
    for ent in doc.ents:
        keywords.add(ent.text.lower())
    return list(keywords)

def calculate_keyword_score(student_text, expected_keywords):
    """
    Calculates what percentage of expected keywords are found in the text.
    """
    if not expected_keywords:
        return 100.0 # If no keywords specified, full points for keywords

    student_text_lower = student_text.lower()
    found_count = 0
    for kw in expected_keywords:
        # Check if the keyword exists as a whole word or phrase
        if re.search(r'\b' + re.escape(kw.lower()) + r'\b', student_text_lower):
            found_count += 1
            
    return (found_count / len(expected_keywords)) * 100.0
