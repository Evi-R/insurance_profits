""" Calculates the profits from the perspective of an insurance
company of the German Health Insurance.

The project consists of two separate parts:
    part 1: calculates discounted profits
        from input data
        for all possible entry ages and
        stores them into a file "discounted_profits",
    part 2: calculates prtfolio profits
    from portfolio input data and
        discounted profits from part 1 and 
        displays the results in a table and bar chart.

This module asks the user wheter both parts or only part 2 should be calculated. 
The answers are entered via the keyboard.
"""

from calculate_discounted_profits import calculate_discounted_profits
from calculate_portfolio_profits import calculate_portfolio_profits

update_input_values = input("Update input values? Please type 'yes' or 'no':  ")
if update_input_values == "yes":
    calculate_discounted_profits()
    print("Input values updated")
    calculate_portfolio_profits()
elif update_input_values == "no":
    calculate_portfolio_profits()
else:
    print("No correct input for input update, please try again")
