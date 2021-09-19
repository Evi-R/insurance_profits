""" Calculates further contract values from the input values

    The function shift_one_right_set_1 is designed for 2-dimensional arrays,
    but it works for a 1-dimensional array taken as
    a 2-dimensional 1 by n array.
"""

import numpy as np
from load_input_values import *
from functions_for_2_to_2_dim_arrays import *

contr_continued = 1 - contr_mortality - contr_lapse
contr_number_of_insured = (np.cumprod(
                    shift_one_right_set_1(contr_continued.reshape(1, n))))
contr_discount_factor = np.cumprod(1 / (1 + contr_interest))
contr_discounted_number_of_insured = (contr_number_of_insured
                                      * contr_discount_factor)
contr_annuity_value = (reverse_cumsum(contr_discounted_number_of_insured)
                       / contr_discounted_number_of_insured)
contr_benefit_value = (reverse_cumsum(contr_discounted_number_of_insured
                       * contr_medical_expenses)
                       / contr_discounted_number_of_insured)
contr_premium = ((contr_benefit_value / contr_annuity_value)
                 / (1 - contr_safety_margin))
