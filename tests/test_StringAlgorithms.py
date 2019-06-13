"""Testing the functions in the pattern_counting module
"""
import pytest
from BioAlgo import StringAlgorithms


def test_pattern_count():
    assert StringAlgorithms.pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == 3

def test_frequent_words():
    assert StringAlgorithms.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == ['ACTAT']

def test_fast_frequent_words():
    assert StringAlgorithms.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == ['ACTAT']

def test_pattern_to_number():
    assert StringAlgorithms.pattern_to_number("AGT") == 11

def test_number_to_pattern():
    assert StringAlgorithms.number_to_pattern(11, 3) == "AGT"