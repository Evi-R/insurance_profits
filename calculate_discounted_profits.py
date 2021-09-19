import numpy as np
from calculate_contract_values import *
from functions_for_1_to_2_dim_arrays import *
from functions_for_2_to_2_dim_arrays import *


def calculate_discounted_profits():
    """ Calculates discounted profits and stores them in a file.

    Loads 1-dim arrays from "calculate_contract_values",
    calculates discounted_profits for all entry ages as a 1-dim numpy array,
    stores them into file "discounted_profits".

    Args:
        None

    Returns:
        None
    """

    medical_expenses = triangular(arrange_diagonally(contr_medical_expenses))
    safety_margin = triangular(arrange_diagonally(contr_safety_margin))
    policyholder_share = triangular(
                             arrange_diagonally(contr_policyholder_share))
    annuity_value = triangular(arrange_diagonally(contr_annuity_value))
    continued = triangular(arrange_diagonally(contr_continued))
    interest = triangular(arrange_in_rows(contr_interest))
    premium = triangular(arrange_in_columns(contr_premium))
    deduction = (triangular(arrange_diagonally(contr_premium)) - premium)
    shifted_diagonal_continued = triangular(shift_one_right_set_1(
                                     arrange_diagonally(contr_continued)))
    number_of_insured = np.cumprod(shifted_diagonal_continued, axis=1)
    calc_reserve = shift_one_left_set_0(
                       deduction * annuity_value * (1 - safety_margin))
    reserve = number_of_insured * (continued * calc_reserve / (1 + interest))
    in_flow = number_of_insured * premium
    out_flow = number_of_insured * (medical_expenses + premium
                                    * policyholder_share * safety_margin)

    # the calculation for assets and reserves is based
    # on the opposite previously calculated value.
    assets = in_flow - out_flow
    profits = assets - reserve
    for i in range(1, n):
        assets[:, i] += ((assets[:, i - 1] - profits[:, i - 1])
                         * (1 + interest[:, i - 1]))
        profits[:, i] = assets[:, i] - reserve[:, i]

    discount_factor = np.cumprod(
                      shift_one_right_set_1(1 / (1 + interest)), axis=1)

    discounted_profits = np.sum((discount_factor * profits), axis=1)
    np.save('discounted_profits/discounted_profits', discounted_profits)

    return None
