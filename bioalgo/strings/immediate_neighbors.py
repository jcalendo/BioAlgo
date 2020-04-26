def immediate_neighbors(pattern: str) -> List[str]:
    """Generate a list of neightbors whose hamming distance is 1 from the pattern
    
    Arguments:
        pattern {str} -- pattern to generate neighborhood from

    Returns:
        List[str] -- 1-neighborhood list of pattern

    Example:
    >>> immediate_neighbors("CAA")
    ['CAA', 'AAA', 'GAA', 'TAA', 'CCA', 'CGA', 'CTA', 'CAC', 'CAG', 'CAT']
    
    """
    neighbors = [pattern]
    bases = ["A", "C", "G", "T"]
    for i in range(len(pattern)):
        symbol = pattern[i]
        for base in bases:
            if symbol != base:
                pattern_list = list(pattern)
                pattern_list[i] = base
                neighbors.append("".join(pattern_list))

    return neighbors