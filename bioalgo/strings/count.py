"""
Module for counting the occurences of patterns within a given text
"""
from typing import Dict
from collections import Counter


def pattern_count(text: str, pattern: str) -> int:
    """Count the number of occurences of a pattern within text
    
    Arguments:
        text {str} -- text to count pattern in
        pattern {str} -- pattern to be counted within text
    """
    count  = 0
    pattern_size = len(pattern)

    for i in range(len(text) - pattern_size):
        if text[i:i+pattern_size] == pattern:
            count += 1
    
    return count


def pattern_index(text: str, pattern: str) -> int:
    """Return the indeces (1-based) of a pattern within text
    
    Arguments:
        text {str} -- text to search for pattern
        pattern {str} -- pattern to search for in text
    
    Returns:
        int -- index location of pattern in text
    """
    indeces = []
    pattern_size = len(pattern)

    for i in range(len(text) - pattern_size):
        if text[i:i+pattern_size] == pattern:
            indeces.append(i+1)
    
    return indeces


def gc_content(text: str) -> float:
    """Return the GC content of the given text
    
    Arguments:
        text {str} -- DNA string
    
    Returns:
        float -- GC content rounded to 5 decimal places
    """
    counts = Counter(text)
    gc_count = int(counts['G'] + counts['C'])
    gc_content = round(gc_count / len(text) * 100, 5)

    return gc_content


def nucleotides(text: str) -> Dict[str, int]:
    """Return the count of nuceotides within text
    
    Arguments:
        text {str} -- text to count
    
    Returns:
        Dict[str, int] -- Counts of nucleotides within text
    """ 
    return dict(Counter(text.upper()))
