from typing import List
from collections import Counter

from bioalgo.strings.neighbors import neighbors
from bioalgo.strings.pattern_to_number import pattern_to_number


def frequent_words_with_mismatches(text: str, k: int, d: int) -> List[str]:
    """Find the most frequent words in a given text allowing mismatches.

    Arguments:
        text {str} -- text string to search
        k {int} -- kmer size
        d {int} -- number of mismatches

    Returns:
        List[str] -- list of k-mers that occur the maximum number of times
    
    Example:
    >>> frequent_words_with_mismatches("ACAACTATGCATACTATCGGGAACTATCCT", 5, 0)
    ['ACTAT']
    """
    neighborhoods = []
    for i in range(len(text) - k + 1):
        neighborhoods.append(neighbors(text[i:i+k], d))

    # form a single list holding all strings in neighborhoods
    neighborhood_array = [neighbor for neighborhood in neighborhoods for neighbor in neighborhood]

    occurences = Counter(neighborhood_array)

    # return the max number of occurences -- could be more than one key with this value
    max_occurences = occurences[max(occurences, key=occurences.get)]

    # return all of the top occurences
    frequent_words = [k for k, v in occurences.items() if v == max_occurences]

    return frequent_words