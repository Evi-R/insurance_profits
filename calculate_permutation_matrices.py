
""" Generates quadratic matrices for functions that use an
index permutation, or set entries equal to zero.

Creates square 2-dim numpy arrays with the entries 0, ..., n - 1,
which are arranged according to certain patterns.
These matrices are used later for the functions.
The size of the arrays n is passed from "load input date".

This module was purposely not written as functions,
because one has to calculate the matrices only once.
Later they could be stored in the separate file and read out.
"""

import numpy as np
from functions_for_1_to_1_dim_arrays import *
from functions_for_0_to_1_dim_arrays import *
from load_input_values import n

permutation_matrix_diagonally = np.array(
                    [rotate_left_array(np.arange(n), i) for i in range(n)])
permutation_matrix_rows = np.array([np.arange(n) for i in range(n)])
permutation_matrix_columns = np.array([n * [i] for i in range(n)])
triangular_zero_matrix = np.array([one_zero_array(n, i) for i in range(n)])
