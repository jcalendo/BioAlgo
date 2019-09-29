"""
Module for finding and profiling motifs in lists of DNA strings
"""
from typing import List, Dict


def count_matrix(motifs: List[str]) -> Dict:
    """Return the count matrix from a list of dna strings of equal length
    
    Arguments:
        motifs {List[str]} -- List of DNA sequences of equal length
    
    Returns:
        Dict -- count matrix
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