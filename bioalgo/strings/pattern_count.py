def pattern_count(text: str, pattern: str) -> int:
    """Count the number of occurences of a pattern within text
    
    Arguments:
        text {str} -- text to count pattern in
        pattern {str} -- pattern to be counted within text

    Returns:
        int -- The number of occurences of pattern in the test

    Example:
    >>> pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT")
    3

    """
    count  = 0
    pattern_size = len(pattern)

    for i in range(len(text) - pattern_size + 1):
        if text[i:i+pattern_size] == pattern:
            count += 1
    
    return count