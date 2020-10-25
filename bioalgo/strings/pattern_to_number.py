def pattern_to_number(pattern: str) -> int:
    """"Transform a k-mer pattern into an integer
    
    Arguments:
        pattern {str} -- text to convert
    
    Returns:
        int -- numerical representation of pattern

    Example:
    >>> pattern_to_number("AGT")
    11
    
    """
    if not pattern:
        return 0

    symbols = {"A":0, "C":1, "G":2, "T":3}
    symbol = pattern[-1]
    prefix = pattern[:-1]

    return 4 * pattern_to_number(prefix) + symbols.get(symbol)