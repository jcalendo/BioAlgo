def compute_skew(sequence: str) -> List[float]:
    """Find the skew of the given sequence
    
    Arguments:
        sequence {str} -- DNA string
    
    Returns:
        List[float] -- skew list
    """
    running_skew = []
    skew = 0

    for base in sequence.upper():
        if base == "G":
            skew += 1
        elif base == "C":
            skew -= 1
        else:
            skew += 0

        running_skew.append(skew)

    return running_skew