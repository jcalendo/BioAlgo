"""
Module for converting numbers to patterns and vice versa
"""
from itertools import product


def number_to_pattern_pythonic(index: int, k: int) -> str:
    """Convert a number to its pattern representation using itertools 
    cartesian product
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    """
    return "".join(list(product("ACGT", repeat=k))[index])


def number_to_pattern(index: int, k: int) -> str:
    """Convert an integer to its pattern representation
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    """
    symbols = ["A", "C", "G", "T"]

    if k == 1:
        return symbols[index]

    prefix_index = index // 4
    r = index % 4
    symbol = symbols[r]

    prefix_pattern = number_to_pattern(prefix_index, k-1)

    return prefix_pattern + symbol


def pattern_to_number_pythonic(pattern: str) -> int:
    """Transform a k-mer pattern into an integer using itertools product
    
    Arguments:
        pattern {str} -- text to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    if not pattern:
        return 0

    k = len(pattern)
    patterns = ["".join(p) for p in list(product("ACGT", repeat=k))]

    return patterns.index(pattern)


def pattern_to_number(pattern: str) -> int:
    """"Transform a k-mer pattern into an integer
    
    Arguments:
        pattern {str} -- text to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    if not pattern:
        return 0

    symbols = {"A":0, "C":1, "G":2, "T":3}
    symbol = pattern[-1]
    prefix = pattern[:-1]

    return 4 * pattern_to_number(prefix) + symbols.get(symbol)
