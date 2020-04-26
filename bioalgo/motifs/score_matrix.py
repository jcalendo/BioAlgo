from strings import hamming_distance


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