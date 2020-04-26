from typing import Dict


def compute_frequencies(text: str, k: int) -> Dict[str, int]:
    """Return the frequency array (count of each k-mer) in a given text 
    
    Arguments:
        text {str} -- text to seacrh
        k {int} -- k-mer length
    
    Returns:
        Dict[str, int] -- dictionary of k-mers and their count within text

    Example:
    >>> compute_frequencies("ACGT", 2)
    {'AC': 1, 'CG': 1, 'GT': 1}
    
    """
    frequency_dict = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        frequency_dict[pattern] = frequency_dict.get(pattern, 0) + 1

    return frequency_dict