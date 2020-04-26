from typinf import List


def insert_kmer(text: List[str], kmer: str, mutations: int = 0) -> List[str]:
    """Randomly insert the given kmer with n mutations into each string in the list of DNA strings. 
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