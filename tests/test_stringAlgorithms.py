"""
Testing the functions in the stringAlgorithms module
"""
import pytest
from BioAlgo.stringAlgorithms import patternCount, frequentWords, patternToNumber, numberToPattern, reverseComplement


def test_pattern_count():
    assert patternCount.pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == 3

def test_frequent_words():
    assert frequentWords.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_fast_frequent_words():
    assert frequentWords.fast_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_pattern_to_number():
    assert patternToNumber.pattern_to_number("AGT") == 11

def test_pattern_to_number_pythonic():
    assert patternToNumber.pattern_to_number_pythonic("GCGGTAA") == 9904

def test_number_to_pattern():
    assert numberToPattern.number_to_pattern(11, 3) == "AGT"

def test_number_to_pattern_pythonic():
    assert numberToPattern.number_to_pattern_pythonic(9904, 7) == "GCGGTAA"

def test_sorted_frequent_words():
    assert frequentWords.sorted_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_reverse_complement():
    assert reverseComplement.reverse_complement("AGTCGCATAGT") == "ACTATGCGACT"

