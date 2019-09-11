"""
Module for visualizing data
"""
from typing import List

import matplotlib.pyplot as plt

from bioalgo.strings import count


def skew(sequence: str):
    """Plot the skew diagram for the given sequence
    
    Arguments:
        sequence {str} -- DNA sequence
    """
    skew_list = count.compute_skew(sequence)
    positions = [x for x in range(len(sequence))]

    # plot the skew
    plt.plot(positions, skew_list)
    plt.title("Skew Diagram")
    plt.xlabel("Position")
    plt.ylabel("Skew")
    plt.show()
