import numpy as np


def one_zero_array(length, i):
    """ Creates a 1-dimensional array with (length - i) ones and i zeros.

    Args:
        length: length of the array
        i: number of zeros

    Returns:
        1-dimensional numpy array
    """
    x1 = np.ones(length - i)
    x2 = np.zeros(i)
    return np.concatenate([x1, x2])
