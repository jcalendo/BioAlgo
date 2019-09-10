"""
Module for identifying frequent patterns within a given text
"""
from typing import Set, Dict
from itertools import product

from count import pattern_count
from convert import pattern_to_number, number_to_pattern


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


def fast_frequent_words(text: str, k: int) -> Set[str]:
    """Find the most frequent kmers of size k in the given text looping
    through text only once.
    
    Arguments:
        text {str} -- text to search
        k {int} -- k-mer size
    
    Returns:
        Set[str] -- most frequent k-mers in text

    Example:
    >>> fast_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5)
    {'ACTAT'}
    
    """
    frequent_patterns = set()
    kmers = list(product("ACGT", repeat=k))
    freq_dict = {"".join(m):0 for m in kmers}

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        freq_dict[pattern] += 1

    max_count = max(freq_dict.values())

    for k in freq_dict:
        if freq_dict[k] == max_count:
            frequent_patterns.add(k)

    return frequent_patterns


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


def compute_frequencies(text: str, k: int) -> Dict[str, int]:
    """Return the frequency array (count of each k-mer) in a given text 
    
    Arguments:
        text {str} -- text to seacrh
        k {int} -- k-mer length
    
    Returns:
        Dict[str, int] -- dictionary of k-mers and their count within text

    Example:
    >>> compute_frequencies("ACGT", 2)
    {'AC': 1, 'CG': 1, 'GT': 1}
    
    """
    frequency_dict = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        frequency_dict[pattern] = frequency_dict.get(pattern, 0) + 1

    return frequency_dict