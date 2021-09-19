""" Loads input values and converts them to 1-dim numpy arrays.

    The input values are stored in text files,
    these should contain the same number of lines/values.

    Calculates the length of the arrays n as the length of medical_expenses.
"""

import numpy as np

contr_medical_expenses = np.genfromtxt("input_values/medical_expenses.txt")
contr_mortality = np.genfromtxt("input_values/mortality.txt")
contr_lapse = np.genfromtxt("input_values/lapse.txt")
contr_safety_margin = np.genfromtxt("input_values/safety_margin.txt")
contr_policyholder_share = np.genfromtxt("input_values/policyholder_share.txt")
contr_interest = np.genfromtxt("input_values/interest.txt")

n = len(contr_medical_expenses)
