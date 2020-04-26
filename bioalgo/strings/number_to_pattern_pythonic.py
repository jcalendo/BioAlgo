from itertools import product


def number_to_pattern_pythonic(index: int, k: int) -> str:
    """Convert a number to its pattern representation using itertools 
    cartesian product
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    
    Example:
    >>> number_to_pattern_pythonic(9904, 7)
    'GCGGTAA'

    """
    return "".join(list(product("ACGT", repeat=k))[index])