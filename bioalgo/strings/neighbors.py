from typing import Set

from bioalgo.strings.hamming_distance import hamming_distance


def neighbors(pattern: str, d: int) -> Set:
    """Generate the d-neighborhood of a kmer pattern

    Arguments:
        pattern {str} -- kmer to generate neighborhood
        d {int} -- number of mismatches

    Returns:
        Set -- d-neighborhood of the kmer

    Example:
    >>> neighbors('AT', 1)
    {'GT', 'TT', 'AG', 'AC', 'AT', 'AA', 'CT'}
    
    """
    if d == 0:
        res = set()
        res.add(pattern)
        return res

    if len(pattern) == 1:
        return(set(['A', 'C', 'G', 'T']))

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for s in suffix_neighbors:
        if hamming_distance(pattern[1:], s) < d:
            for n in ['A', 'C', 'G', 'T']:
                neighborhood.add(str(n + s))
        else:
            neighborhood.add(str(pattern[0] + s))

    return neighborhood
