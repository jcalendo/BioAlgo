"""
Module for converting numbers to patterns and vice versa
"""
from itertools import product
from typing import List


def number_to_pattern_pythonic(index: int, k: int) -> str:
    """Convert a number to its pattern representation using itertools 
    cartesian product
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    """
    return "".join(list(product("ACGT", repeat=k))[index])


def number_to_pattern(index: int, k: int) -> str:
    """Convert an integer to its pattern representation
    
    Arguments:
        index {int} -- integer to convert to pattern
        k {int} -- size of pattern

    Returns:
        str -- pattern
    """
    symbols = ["A", "C", "G", "T"]

    if k == 1:
        return symbols[index]

    prefix_index = index // 4
    r = index % 4
    symbol = symbols[r]

    prefix_pattern = number_to_pattern(prefix_index, k-1)

    return prefix_pattern + symbol


def pattern_to_number_pythonic(pattern: str) -> int:
    """Transform a k-mer pattern into an integer using itertools product
    
    Arguments:
        pattern {str} -- text to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    if not pattern:
        return 0

    k = len(pattern)
    patterns = ["".join(p) for p in list(product("ACGT", repeat=k))]

    return patterns.index(pattern)


def pattern_to_number(pattern: str) -> int:
    """"Transform a k-mer pattern into an integer
    
    Arguments:
        pattern {str} -- text to convert
    
    Returns:
        int -- numerical representation of pattern
    """
    if not pattern:
        return 0

    symbols = {"A":0, "C":1, "G":2, "T":3}
    symbol = pattern[-1]
    prefix = pattern[:-1]

    return 4 * pattern_to_number(prefix) + symbols.get(symbol)


def compress_DNA(text: str) -> int:
    """Compress a DNA string into a bit string
    
    Arguments:
        text {str} -- DNA string to compress
    
    Returns:
        int -- integer bit-string representing DNA
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


def decompress_DNA_bit_string(bit_string: int) -> str:
    """Decompress a bit string representation of DNA into a string representation
    
    Arguments:
        bit_string {int} -- bit string DNA representation
    
    Returns:
        str -- DNA text string
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


def imediate_neighbors(pattern: str) -> List[str]:
    """Generate a list of neightbors whose hamming distance is 1 from the pattern
    
    Arguments:
        pattern {str} -- pattern to generate neighborhood from

    Returns:
        List[str] -- 1-neighborhood list of pattern
    """
    neighbors = []
    bases = ["A", "C", "G", "T"]
    for i in range(len(pattern)):
        symbol = pattern[i]
        for base in bases:
            if symbol != base:
                pattern_list = list(pattern)
                pattern_list[i] = base
                neighbors.append("".join(pattern_list))

    return neighbors
