from collections import defaultdict


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