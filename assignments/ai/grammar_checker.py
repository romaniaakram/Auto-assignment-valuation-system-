import language_tool_python

def check_grammar(text):
    """
    Checks the text for grammatical and spelling errors using LanguageTool.
    Returns a grammar score out of 100 and a list of specific feedback items.
    """
    if not text.strip():
        return 0.0, ["Text is empty."]
    
    # Run locally (it will download a java server the first time it is run)
    tool = language_tool_python.LanguageTool('en-US')
    
    matches = tool.check(text)
    
    feedback = []
    for match in matches:
        feedback.append(
            f"Error at character {match.offset}: {match.ruleIssueType} - {match.message}. "
            f"Suggested fix: {', '.join(match.replacements[:3])}"
        )
    
    # Calculate a score based on error density
    # We penalize based on number of errors per 100 characters.
    # This is a heuristic.
    text_len = len(text)
    if text_len == 0:
        return 0.0, feedback
        
    error_density = len(matches) / (text_len / 100.0)
    
    # For every error per 100 chars, we deduct 5 points.
    score = 100.0 - (error_density * 5.0)
    
    if score < 0.0:
        score = 0.0
        
    return score, feedback
