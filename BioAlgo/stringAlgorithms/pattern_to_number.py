def pattern_to_number(pattern: str) -> int:
    """Transform a k-mer pattern into an integer
    
    Arguments:
        pattern {str} -- text pattern to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    symbols = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}

    if not pattern:
        return 0
    
    symbol = pattern.upper()[-1]
    prefix = pattern.upper()[:-1]

    return 4 * pattern_to_number(prefix) +  symbols.get(symbol)