import numpy as np


def rotate_left_array(arr, i):
    """ Rotates 1-dimensional array i places to the left.

    Args:
        arr: 1-dim numpy array
        i: integer for the shift length

    Returns:
        rotated 1-dim numpy array
    """
    x1 = arr[i: len(arr)]
    x2 = arr[0: i]
    return np.concatenate([x1, x2])


def rotate_right_array(arr, i):
    """ Rotates 1-dimensional array i places to the right.

    Args:
        arr: 1-dim numpy array
        i: integer for the shift length

    Returns:
        rotated 1-dim numpy array
    """
    x1 = arr[len(arr) - i: len(arr)]
    x2 = arr[0: len(arr) - i]
    return np.concatenate([x1, x2])


def reverse_cumsum(arr):
    """ Calculates cumulative sum backwards.

    Args:
        arr: 1-dim numpy array

    Returns:
        1-dim numpy array, cumulative sum backwards
    """
    return np.flip(np.cumsum(np.flip(arr)))
