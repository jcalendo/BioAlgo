"""
Module for string manipulations
"""


def reverse_complement(pattern: str) -> str:
    """Return the reverse complement of the input pattern
    
    Arguments:
        pattern {str} -- DNA string
    
    Returns:
        str -- Reverse complement
    """
    transtab = {"A":"T", "C":"G", "G":"C", "T":"A"}

    return "".join(transtab[b] for b in pattern[::-1].upper())