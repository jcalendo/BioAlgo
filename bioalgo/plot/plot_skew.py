from typing import List

import matplotlib.pyplot as plt

from strings import compute_skew



def plot_skew(sequence: str):
    """Plot the skew diagram for the given sequence
    
    Arguments:
        sequence {str} -- DNA sequence
    """
    skew_list = compute_skew.compute_skew(sequence)
    positions = [x for x in range(len(sequence))]

    # plot the skew
    plt.plot(positions, skew_list)
    plt.title("Skew Diagram")
    plt.xlabel("Position")
    plt.ylabel("Skew")
    plt.show()
