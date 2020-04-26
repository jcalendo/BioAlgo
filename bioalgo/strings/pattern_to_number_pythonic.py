from itertools import product


def pattern_to_number_pythonic(pattern: str) -> int:
    """Transform a k-mer pattern into an integer using itertools product
    
    Arguments:
        pattern {str} -- text to convert
    
    Returns:
        int -- numerical representation of pattern

    Example:
    >>> pattern_to_number_pythonic("GCGGTAA")
    9904
    
    """
    if not pattern:
        return 0

    k = len(pattern)
    patterns = ["".join(p) for p in list(product("ACGT", repeat=k))]

    return patterns.index(pattern)