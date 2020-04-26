from typing import Set
from pattern_count import pattern_count


def frequent_words(text: str, k: int) -> Set[str]:
    """Find the most frequent kmers of size k in the given text
    
    Arguments:
        text {str} -- text to find k-mer in
        k {int} -- size of k-mer
    
    Returns:
        Set[str] -- Set of most frequent k-mers found in text
    
    Example:
    >>> frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5)
    {'ACTAT'}
    
    """
    frequent_patterns = set()
    counts = []

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        counts.append(pattern_count(text, pattern))

    max_count = max(counts)

    for i in range(len(text) - k + 1):
        if counts[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    
    return frequent_patterns