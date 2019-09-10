"""
Module for string manipulations
"""


def reverse_complement(pattern: str) -> str:
    """Return the reverse complement of the input pattern
    
    Arguments:
        pattern {str} -- DNA string
    
    Returns:
        str -- Reverse complement

    Example:
    >>> reverse_complement("AGTCGCATAGT")
    'ACTATGCGACT'

    """
    transtab = {"A":"T", "C":"G", "G":"C", "T":"A"}

    return "".join(transtab[b] for b in pattern[::-1].upper())


def transcribe(text: str) -> str:
    """transcribe a DNA string to RNA
    
    Arguments:
        text {str} -- DNA text string
    
    Returns:
        str -- transcribed RNA string
    """
    transtab = {"A":"A", "C":"C", "G":"G", "T":"U"}

    return "".join(transtab[t] for t in text.upper())


def translate(text: str) -> str:
    """Translate an mRNA tring to protein
    
    Arguments:
        text {str} -- mRNA text string
    
    Returns:
        str -- protein string
    """

    codon_table = {'UUU': 'F', 'UUC':'F', 'UUA': 'L', 'UUG':'L', 'UCU': 'S', 
                   'UCC': 'S', 'UCA': 'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 
                   'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 
                   'UGG': 'W', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P',
                   'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 
                   'CAG': 'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 
                   'AUC':'I', 'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 
                   'ACG':'T', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 
                   'AGC':'S', 'AGA':'R', 'AGG':'R', 'GUU':'V', 'GUC':'V', 'GUA':'V',
                   'GUG':'V', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'GAU':'D',
                   'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G', 'GGA':'G', 
                   'GGG':'G'}

    # split string into a list of codons
    codons = [text[i:i+3] for i in range(0, len(text), 3)]

    # check to see if every element in codons is divisible by three
    # if not exit
    for codon in codons:
        if int(len(codon) / 3) == 1:
            continue
        else:
            print(f"Codon: '{codon}' at index {codons.index(codon)} not divisible by 3. Exiting")
            exit(1)

    prot = ''.join([codon_table.get(codon) for codon in codons])

    # remove 'Stop' codon from final string if present
    return prot[:-4] if prot[-4:] == 'Stop' else prot
