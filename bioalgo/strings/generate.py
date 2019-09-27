"""
Module used generate random strings and insert random k-mers
"""
import random
from typing import List


def random_DNA(n: int = 10, length: int = 10) -> List[str]:
    """Generate n DNA strings of length l
    
    Keyword Arguments:
        n {int} -- number of strings to randomly generate (default: {10})
        length {int} -- length of each randomly generated string (default: {600})
    
    Returns:
        List[str] -- list of randomly generated DNA strings
    
    Example:
    >>> random.seed(123)
    >>> random_DNA(1, 10)
    ['AGATGAATGG', 'ACCGGCCATA']

    """
    bases = ['A', 'C', 'G', 'T']
    return ["".join([random.choice(bases) for l in range(length)]) for i in range(n)]


def mutate(text: str, n: int) -> str:
    """Mutate a string text n times
            text {str} -- [description]

    Arguments:
        text {str} -- the string to mutate
        n {int} -- number of mutations to add to string
    
    Returns:
        str -- string with n mutations
    """
    if not n:
        return text

    if n > len(text):
        raise ValueError("Number of mutations greater than the length of the string")
    
    positions = list(range(len(text)))  # indeces in the kmer
    random.shuffle(positions)           # randomly swap the indeces
    mutate_at = [positions.pop() for _ in range(n)]  # get n non-repeating random indeces

    bases = ['A', 'C', 'G', 'T']
    kmer = list(text)
    for position in mutate_at:
        current = kmer[position]
        mutation = random.choice(bases)
        while current == mutation:       # ensure that same base hasn't mutated back
            mutation = random.choice(bases)
        
        kmer[position] = mutation

    return "".join(kmer)


def insert_kmer(text: List[str], kmer: str, mutations: int = 0) -> List[str]:
    """Randomly insert the given kmer with n mutations into the list of DNA strings. 
    Preserve the length of the original text. 
    
    Arguments:
        text {List[str]} -- List of DNA strings to add kmers into
        kmer {str} -- kmer to insert into string
        mutations {int} -- number of random mutations in kmer (default: {0})
    
    Returns:
        List[str] -- List of DNA strings with randomly inserted kmers
    """
    if len(kmer) >= len(text[0]):
        raise ValueError(f"{kmer} is longer than or equivalent in length to DNA strings")

    if mutations >= len(kmer):
        raise ValueError(f"Number of mutations is larger than size of the kmer")

    # check if all DNA strings are the same length
    it = iter(text)
    lens = len(next(it))
    if not all(len(l) == lens for l in it):
        raise ValueError('Not DNA strings have same length!')

    mutated_strings = []
    for t in text:
        start_index = random.randint(0, len(t) - len(kmer))
        kmer = mutate(kmer, mutations)
        new_string = t[:start_index] + kmer + t[start_index + len(kmer):]
        mutated_strings.append(new_string)

    return mutated_strings