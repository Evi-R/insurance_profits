import numpy as np
from calculate_permutation_matrices import *


def triangular(arr):
    """ Sets the entries of the 2-dim array
    located in the lower right corner to 0.

    Args:
        2-dim numpy array

    Returns:
        2-dim numpy array with zeros in the lower right half.
    """
    return arr * triangular_zero_matrix


def shift_one_left_set_0(arr):
    """ Shifts all columns one to the left and fills
    the last column with entries equal to 0.

    Args:
        2-dim numpy array

    Returns:
        2-dim numpy array shifted one to the left with zeros in the last column
    """

    n = len(arr)
    x1 = arr[:, 1:]
    x2 = np.zeros(n).reshape(n, 1)
    return np.concatenate([x1, x2], axis=1)


def shift_one_right_set_1(arr):
    """ Shifts all columns one to the right and fills
    the last column with entries equal to 1.

    Args:
        2-dim numpy array

    Returns:
        2-dim numpy array shifted one to the right with ones in the last column
    """

    n = len(arr)
    x1 = np.ones(n).reshape(n, 1)
    x2 = arr[:, 0: -1]
    return np.concatenate([x1, x2], axis=1)


def set_last_column_as_first(arr):
    """ Shifts the array one to the right and moves the last column
    to the 0-th position.

    Args:
        2-dim numpy array

    Returns:
        2-dim numpy array with the last column at the 0-th position
    """
    n = len(arr)
    x1 = arr[:, -1: n]
    x2 = arr[:, 0: -1]
    return np.concatenate([x1, x2], axis=1)
