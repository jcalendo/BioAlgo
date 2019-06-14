"""Testing the functions in the pattern_counting module
"""
import pytest
from BioAlgo import stringAlgorithms


def test_pattern_count():
    assert stringAlgorithms.pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == 3

def test_frequent_words():
    assert stringAlgorithms.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_fast_frequent_words():
    assert stringAlgorithms.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_pattern_to_number():
    assert stringAlgorithms.pattern_to_number("AGT") == 11

def test_pattern_to_number_pythonic():
    assert stringAlgorithms.pattern_to_number_pythonic("GCGGTAA") == 9904

def test_number_to_pattern():
    assert stringAlgorithms.number_to_pattern(11, 3) == "AGT"

def test_number_to_pattern_pythonic():
    assert stringAlgorithms.number_to_pattern_pythonic(9904, 7) == "GCGGTAA"

def test_sorted_frequent_words():
    assert stringAlgorithms.sorted_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_reverse_complement():
    assert stringAlgorithms.reverse_complement("AGTCGCATAGT") == "ACTATGCGACT"

