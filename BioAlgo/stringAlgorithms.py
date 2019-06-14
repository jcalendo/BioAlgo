"""Collection of algorithms that operate on strings of text -- mainly for counting k-mers
"""
from typing import Set
from itertools import product


def reverse_complement(pattern: str) -> str:
    """Return the reverse complement of the input pattern
    
    Arguments:
        pattern {str} -- DNA string
    
    Returns:
        str -- Reverse complement
    """
    transtab = {"A":"T", "C":"G", "G":"C", "T":"A"}

    return "".join(transtab[b] for b in pattern[::-1].upper())


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


def pattern_to_number(pattern: str) -> int:
    """Transform a k-mer pattern into an integer
    
    Arguments:
        pattern {str} -- text pattern to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    symbols = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}

    if not pattern:
        return 0
    
    symbol = pattern.upper()[-1]
    prefix = pattern.upper()[:-1]

    return 4 * pattern_to_number(prefix) +  symbols.get(symbol)


def pattern_to_number_pythonic(pattern: str) -> int:
    """Transform a k-mer into an interger using itertools product
    
    Arguments:
        pattern {str} -- text pattern to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    k = len(pattern)
    patterns = ["".join(p) for p in list(product("ACGT", repeat=k))]

    return patterns.index(pattern)


def number_to_pattern(index: int, k: int) -> str:
    """Convert an integer to its pattern representation
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    """
    symbols = ["A", "C", "G", "T"]

    if k == 1:
        return symbols[index]

    prefix_index = index // 4
    r = index % 4
    symbol = symbols[r]

    prefix_pattern = number_to_pattern(prefix_index, k-1)

    return prefix_pattern + symbol


def number_to_pattern_pythonic(index: int, k: int) -> str:
    """Convert a number to its pattern representation using itertools 
    cartesian product
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    """
    return "".join(list(product("ACGT", repeat=k))[index])


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