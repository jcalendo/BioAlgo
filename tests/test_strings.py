"""
Testing the functions in the strings module
"""
import pytest
from BioAlgo.strings import convert, count, transform, words


def test_pattern_count():
    assert count.pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == 3

def test_frequent_words():
    assert words.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_fast_frequent_words():
    assert words.fast_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_pattern_to_number():
    assert convert.pattern_to_number("AGT") == 11

def test_pattern_to_number_pythonic():
    assert convert.pattern_to_number_pythonic("GCGGTAA") == 9904

def test_number_to_pattern():
    assert convert.number_to_pattern(11, 3) == "AGT"

def test_number_to_pattern_pythonic():
    assert convert.number_to_pattern_pythonic(9904, 7) == "GCGGTAA"

def test_sorted_frequent_words():
    assert words.sorted_frequent_words("ACAACTATGCATACTATCGGGAACTATCCT", 5) == {'ACTAT'}

def test_reverse_complement():
    assert transform.reverse_complement("AGTCGCATAGT") == "ACTATGCGACT"

