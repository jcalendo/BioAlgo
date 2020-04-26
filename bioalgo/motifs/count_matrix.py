from typing import List


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