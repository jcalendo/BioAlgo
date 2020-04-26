def hamming_distance(str_1: str, str_2: str) -> int:
    """Return the hamming distance between two strings of equal length
    
    Arguments:
        str_1 {str} -- first string
        str_2 {str} -- second string
    
    Returns:
        int -- hamming distance

    Example:
    >>> hamming_distance("ATATACATACGCGCGC", "ATATATATGCGCGCGC")
    2
    
    """
    if len(str_1) != len(str_2):
        raise ValueError("Strings must be the same length")

    count = 0
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            count += 1
        
    return count