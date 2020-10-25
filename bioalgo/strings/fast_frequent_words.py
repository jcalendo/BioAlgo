from itertools import product


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