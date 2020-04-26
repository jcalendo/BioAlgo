def mutate(text: str, n: int) -> str:
    """Mutate a string text n times

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