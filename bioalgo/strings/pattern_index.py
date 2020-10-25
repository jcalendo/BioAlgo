def pattern_index(text: str, pattern: str) -> List[int]:
    """Return the indeces (1-based) of a pattern within text
    
    Arguments:
        text {str} -- text to search for pattern
        pattern {str} -- pattern to search for in text
    
    Returns:
        int -- index location of pattern in text

    Example:
    >>> pattern_index("ACAACTATGCATACTATCGGGAACTATCCT", "TAT")
    [6, 15, 25]
    
    """
    indeces = []
    pattern_size = len(pattern)

    for i in range(len(text) - pattern_size + 1):
        if text[i:i+pattern_size] == pattern:
            indeces.append(i+1)
    
    return indeces