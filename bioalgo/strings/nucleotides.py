from typing import Dict


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