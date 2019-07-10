"""
Module for identifying frequent patterns within a given text
"""
from typing import Set, Dict
from itertools import product

from count import pattern_count
from convert import pattern_to_number
from convert import number_to_pattern


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


def fast_frequent_words(text: str, k: int) -> Set[str]:
    """Find the most frequent kmers of size k in the given text looping
    through text only once.
    
    Arguments:
        text {str} -- text to search
        k {int} -- k-mer size
    
    Returns:
        Set[str] -- most frequent k-mers in text
    """
    frequent_patterns = set()
    kmers = list(product("ACGT", repeat=k))
    freq_dict = {"".join(m):0 for m in kmers}

    for i in range(len(text) - k):
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
    """
    frequent_patterns = set()
    counts = []

    for i in range(len(text) - k):
        pattern = text[i:i+k]
        counts.append(pattern_count(text, pattern))

    max_count = max(counts)

    for i in range(len(text) - k):
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
    """
    frequency_dict = {}
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        frequency_dict[pattern] = frequency_dict.get(pattern, 0) + 1

    return frequency_dict


def find_clumps(genome: str, k: int, t: int, L: int) -> Set[str]:
    """Return frequent k-mer patterns in genome using a clumps finding
    algorithm. Slide a window of fixed length L along genome, looking
    for regions where a k-mer appears t or more times in the given region.
    
    Arguments:
        genome {str} -- text to search
        k {int} -- k-mer length
        t {int} -- size of the clumps
        L {int} -- window size

    Returns:
        Set[str] -- [description]
    """
    frequent_patterns = set()
    clumps = {}

    text = genome[0:L]
    freq_dict = compute_frequencies(text, k)
    for k, v in freq_dict.items():
        if v >= t:
            clumps[k] = clumps.get(k, 0) + 1

    for i in range(1, genome - L):
        first_pattern = genome[i-1:i-1+k]
        freq_dict[first_pattern] = freq_dict[first_pattern] - 1
        last_pattern = genome[i+L-k:i+L]
        freq_dict[last_pattern] = freq_dict[last_pattern] + 1

    pass