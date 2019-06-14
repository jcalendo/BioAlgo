from itertools import product
from typing import Set

from BioAlgo.stringAlgorithms import pattern_to_number, number_to_pattern


def sorted_frequent_words(text: str, k: int) -> Set[str]:
    """Find the most frequent kmers of size k in the given text by
    sorting
    
    Arguments:
        text {str} -- text to search
        k {int} -- k-mer size
    
    Returns:
        Set[str] -- most frequent k-mers in text
    """
    frequent_patterns = set()
    index = []
    count = []
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        index.append(pattern_to_number(pattern))
        count.append(1)

    sorted_index = sorted(index)

    for i in range(1, len(text) - k):
        if sorted_index[i] == sorted_index[i-1]:
            count[i] = count[i-1] + 1

    max_count = max(count)

    for i in range(len(text) - k):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_patterns.add(pattern)

    return frequent_patterns