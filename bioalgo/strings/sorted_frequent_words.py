from typing import Set

from number_to_pattern import number_to_pattern
from pattern_to_number import pattern_to_number


def sorted_frequent_words(text: str, k: int) -> Set[str]:
    """Find the most frequent kmers of size k in the given text by
    sorting
    
    Arguments:
        text {str} -- text to search
        k {int} -- k-mer size
    
    Returns:
        Set[str] -- most frequent k-mers in text

    Example:
    >>> sorted_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5)
    {'ACTAT'}
    
    """
    frequent_patterns = set()
    index = []
    count = []
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        index.append(pattern_to_number(pattern))
        count.append(1)

    sorted_index = sorted(index)

    for i in range(1, len(text) - k + 1):
        if sorted_index[i] == sorted_index[i-1]:
            count[i] = count[i-1] + 1

    max_count = max(count)

    for i in range(len(text) - k + 1):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_patterns.add(pattern)

    return frequent_patterns
