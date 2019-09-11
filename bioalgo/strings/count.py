"""
Module for counting the occurences of patterns within a given text
"""
from typing import Dict, List
from collections import Counter


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


def gc_content(text: str) -> float:
    """Return the GC content of the given text
    
    Arguments:
        text {str} -- DNA string
    
    Returns:
        float -- GC content rounded to 5 decimal places

    Example:
    >>> gc_content("ACAACTATGCATACTATCGGGAACTATCCT")
    40.0
    
    """
    counts = Counter(text.upper())
    gc_count = int(counts['G'] + counts['C'])
    gc_content = round(gc_count / len(text) * 100, 5)

    return gc_content


def nucleotides(text: str) -> Dict[str, int]:
    """Return the count of nuceotides within text
    
    Arguments:
        text {str} -- text to count
    
    Returns:
        Dict[str, int] -- Counts of nucleotides within text

    Example:
    >>> nucleotides("ACAACTATGCATACTATCGGGAACTATCCT")
    {'A': 10, 'C': 8, 'T': 8, 'G': 4}
    
    """ 
    return dict(Counter(text.upper()))


def hamming_distance(str_1: str, str_2: str) -> int:
    """Return the hamming distance between two strings od equal length
    
    Arguments:
        str_1 {str} -- first string
        str_2 {str} -- second string
    
    Returns:
        int -- hamming distance

    Example:
    >>> hamming_distance("ATATACATACGCGCGC", "ATATATATGCGCGCGC")
    2
    
    """
    if len(str_1) != len(str_2):
        raise ValueError("Strings must be the same length")

    count = 0
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            count += 1
        
    return count


def imediate_neighbors(pattern: str) -> List[str]:
    """Generate a list of neightbors whose hamming distance is 1 from the pattern
    
    Arguments:
        pattern {str} -- pattern to generate neighborhood from

    Returns:
        List[str] -- 1-neighborhood list of pattern
    """
    neighbors = [pattern]
    bases = ["A", "C", "G", "T"]
    for i in range(len(pattern)):
        symbol = pattern[i]
        for base in bases:
            if symbol != base:
                pattern_list = list(pattern)
                pattern_list[i] = base
                neighbors.append("".join(pattern_list))

    return neighbors


def compute_skew(sequence: str) -> List[float]:
    """Find the skew of the given sequence
    
    Arguments:
        sequence {str} -- DNA string
    
    Returns:
        List[float] -- skew list
    """
    running_skew = []
    skew = 0

    for base in sequence.upper():
        if base == "G":
            skew += 1
        elif base == "C":
            skew -= 1
        else:
            skew += 0

        running_skew.append(skew)

    return running_skew