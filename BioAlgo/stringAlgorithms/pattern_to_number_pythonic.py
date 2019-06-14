from itertools import product


def pattern_to_number_pythonic(pattern: str) -> int:
    """Transform a k-mer into an interger using itertools product
    
    Arguments:
        pattern {str} -- text pattern to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    k = len(pattern)
    patterns = ["".join(p) for p in list(product("ACGT", repeat=k))]

    return patterns.index(pattern)