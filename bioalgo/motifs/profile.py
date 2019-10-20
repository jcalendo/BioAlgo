"""
Module for finding and profiling motifs in lists of DNA strings
"""
from typing import List, Dict
from collections import defaultdict

from strings.count import hamming_distance


def count_matrix(motifs: List[str]) -> Dict:
    """Return the count matrix from a list of dna strings of equal length
    
    Arguments:
        motifs {List[str]} -- List of DNA sequences of equal length
    
    Returns:
        Dict -- count matrix

    Example:
    >>> motifs = ["TCGGGGGTTTTT",
    ...           "CCGGTGACTTAC",
    ...           "ACGGGGATTTTC",
    ...           "TTGGGGACTTTT",
    ...           "AAGGGGACTTCC",
    ...           "TTGGGGACTTCC",
    ...           "TCGGGGATTCAT",
    ...           "TCGGGGATTCCT",
    ...           "TAGGGGAACTAC",
    ...           "TCGGGTATAACC"]
    >>> count_mat = count_matrix(motifs)
    >>> for k, v in count_mat.items():
    ...     print(k, v)
    A [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0]
    C [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6]
    G [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0]
    T [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]
    """
    if not all([len(m) == len(motifs[0]) for m in motifs]):
        raise ValueError("All motifs must be same length.")

    count_mat = {"A" : [0 for _ in range(len(motifs[0]))],
                 "C" : [0 for _ in range(len(motifs[0]))],
                 "G" : [0 for _ in range(len(motifs[0]))],
                 "T" : [0 for _ in range(len(motifs[0]))]
                }

    for seq in motifs:
        for i, nt in enumerate(seq):
            count_mat[nt][i] += 1
            
    return count_mat


def profile(count_matrix: Dict) -> Dict:
    """Generate the profile matrix of the given count matrix
    
    Arguments:
        count_matrix {Dict} -- motif count matrix
    
    Returns:
        Dict -- profile matrix of the counts matrix
    
    Example:
    >>> count_matrix = {'A': [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0], 
    ...                 'C': [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6], 
    ...                 'G': [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0], 
    ...                 'T': [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]}
    >>> profile_mat = profile(count_matrix)
    >>> for k, v in profile_mat.items():
    ...     print(k, v)
    A [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0]
    C [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6]
    G [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
    T [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
    """
    # the number of motifs is the sum of all counts in any column - since all columns should be derived
    # from the same number of motifs, simply sum the first column to get the number of motifs
    n_motifs = sum([count_matrix['A'][0], count_matrix['C'][0], count_matrix['G'][0], count_matrix['T'][0]])

    profile = defaultdict(list)
    for k, v in count_matrix.items():
        profile[k] = list(map(lambda x: x / n_motifs, v))

    return dict(profile)


def consensus(profile_matrix: Dict) -> str:
    """Return the consensus by scoring columns in the profile matrix.  
    
    Arguments:
        profile_matrix {Dict} -- profile matrix computed from count matrix
    
    Returns:
        str -- the consensus string

    Example:
    >>> profile_matrix = {'A' : [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    ...                   'C' : [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    ...                   'G' : [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    ...                   'T' : [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
    >>> print(consensus(profile_matrix))
    TCGGGGATTTCC
    """
    consensus = ""
    for i in range(len(profile_matrix['A'])):  # arbitrarily select the 'A' list to get length
        max_freq = 0
        base_called = ""
        for k, v in profile_matrix.items():
            if v[i] > max_freq:
                max_freq = v[i]
                base_called = k

        consensus += base_called

    return consensus


def score(motifs: List[str], consensus_string: str) -> int:
    """Score the motif matrix against a consensus sequence
    
    Arguments:
        motifs {List[str]} --  list of motifs to score
        consensus_string {str} -- The consensus string of the motifs
    
    Returns:
        int -- score
    
    Example:
    >>> motifs = ["TCGGGGGTTTTT",
    ...           "CCGGTGACTTAC",
    ...           "ACGGGGATTTTC",
    ...           "TTGGGGACTTTT",
    ...           "AAGGGGACTTCC",
    ...           "TTGGGGACTTCC",
    ...           "TCGGGGATTCAT",
    ...           "TCGGGGATTCCT",
    ...           "TAGGGGAACTAC",
    ...           "TCGGGTATAACC"]
    >>> cons = "TCGGGGATTTCC"
    >>> print(score(motifs, cons))
    30
    """
    return sum([hamming_distance(m, consensus_string) for m in motifs])
