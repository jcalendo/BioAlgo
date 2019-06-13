"""Testing the functions in the pattern_counting module
"""
import pytest
from BioAlgo import pattern_counting as pc


def test_pattern_count():
    assert pc.pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == 3


def test_frequent_words():
    assert pc.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == ['ACTAT']


def test_fast_frequent_words():
    assert pc.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == ['ACTAT']


def test_pattern_to_number():
    assert pc.pattern_to_number("AGT") == 11