def decompress_dna_bit_string(bit_string: int) -> str:
    """Decompress a bit string representation of DNA into a string representation
    
    Arguments:
        bit_string {int} -- bit string DNA representation
    
    Returns:
        str -- DNA text string

    Example:
    >>> decompress_dna_bit_string(283)
    'ACGT'
    
    """
    dna_string = ""
    for i in range(0, bit_string.bit_length() - 1, 2):  # minus 1 excludes '1' sentinel value from compress_DNA
        bits = bit_string >> i & 0b11
        if bits == 0b00:
            dna_string += "A"
        elif bits == 0b01:
            dna_string += "C"
        elif bits == 0b10:
            dna_string += "G"
        elif bits == 0b11:
            dna_string += "T"
        else:
            raise ValueError(f"Invalid DNA bit: {bits}")

    return dna_string[::-1]