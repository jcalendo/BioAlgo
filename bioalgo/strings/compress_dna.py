def compress_dna(text: str) -> int:
    """Compress a DNA string into a bit string
    
    Arguments:
        text {str} -- DNA string to compress
    
    Returns:
        int -- integer bit-string representing DNA

    Example:
    >>> compress_dna("ACGT")
    283
    
    """

    bit_string = 1

    for nt in text.upper():
        bit_string <<= 2
        if nt == "A":
            bit_string |= 0b00
        elif nt == "C":
            bit_string |= 0b01
        elif nt == "G":
            bit_string |= 0b10
        elif nt == "T":
            bit_string |= 0b11
        else:
            raise ValueError(f'Invalid nucleotide: {nt}')

    return bit_string