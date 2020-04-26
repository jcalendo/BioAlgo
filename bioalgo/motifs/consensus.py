from typing import Dict


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