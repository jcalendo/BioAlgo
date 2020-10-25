from collections import Counter


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