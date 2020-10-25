def number_to_pattern(index: int, k: int) -> str:
    """Convert an integer to its pattern representation
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern

    Example:
    >>> number_to_pattern(11, 3)
    'AGT'

    """
    symbols = ["A", "C", "G", "T"]

    if k == 1:
        return symbols[index]

    prefix_index = index // 4
    r = index % 4
    symbol = symbols[r]

    prefix_pattern = number_to_pattern(prefix_index, k-1)

    return prefix_pattern + symbol