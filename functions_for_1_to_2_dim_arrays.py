from calculate_permutation_matrices import *
from functions_for_2_to_2_dim_arrays import *


def arrange_diagonally(arr):
    """ Arranges 1-dim array in a 2-dim square array diagonally.

    Repeats the 1-dimensional array in rows,
    rotating the array one to the left in each row.

    Args:
        arr: 1-dim numpy array

    Returns:
        2-dim numpy array where the input array is written in every row
        with a shift to the left
    """
    return arr[permutation_matrix_diagonally]


def arrange_in_rows(arr):
    """ Repeats 1-dim array in a 2-dim square array as rows.

    Args:
        arr: 1-dim numpy array

    Returns:
        2-dim numpy array where the input array is written in every row
    """
    return arr[permutation_matrix_rows]


def arrange_in_columns(arr):
    """ Repeats 1-dim array in a 2-dim square array as columns.

    Args:
        arr: 1-dim numpy array

    Returns:
        2-dim numpy array where the input array is written in every column
    """
    return arr[permutation_matrix_columns]
