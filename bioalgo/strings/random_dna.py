import random
from typing import List


def random_DNA(n: int = 10, length: int = 100) -> List[str]:
    """Generate n DNA strings of length l
    
    Keyword Arguments:
        n {int} -- number of strings to randomly generate (default: {10})
        length {int} -- length of each randomly generated string (default: {100})
    
    Returns:
        List[str] -- list of randomly generated DNA strings
    
    Example:
    >>> random.seed(123)
    >>> random_DNA(2, 10)
    ['AGATGAATGG', 'ACCGGCCATA']

    """
    bases = ['A', 'C', 'G', 'T']
    return ["".join([random.choice(bases) for l in range(length)]) for i in range(n)]