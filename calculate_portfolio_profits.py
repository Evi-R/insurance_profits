import numpy as np
import matplotlib.pyplot as plt


def calculate_portfolio_profits():
    """ Calsulates portfolio profits for a given protfolio.

        Asks for a keyboard input of portfolio number,
        loads portfolio data and discounted_profits.

        Prints a table with portfolio data and
        the corresponding profits and
        creates a bar chart with the profits depending
        on the entry ages.

    Args:
        None

    Returns:
        None
    """

    portfolio_number = input("Please enter portfolio number (1, 2 or 3):  ")
    portfolio_values = np.genfromtxt(
                "portfolio_values/portfolio"
                + str(portfolio_number)
                + ".txt")
    discounted_profits = np.load('discounted_profits/discounted_profits.npy')
    portfolio_profits = portfolio_values * discounted_profits

    n = len(portfolio_values)
    print("----------------------------------")
    print(" {:6} | {:9} | {:8} ".format("Entry", "Number of", "Entity's"))
    print(" {:6} | {:9} | {:8} ".format("age", "insured", "profits"))
    print("----------------------------------")
    for i in range(n):
        print(" {:6} | {:9} | {:8} ".format(
              i,
              int(portfolio_values[i]),
              round(portfolio_profits[i], 2)))
    print("----------------------------------")
    print(" {:6} | {:9} | {:8} ".format(
          "Sum",
          int(np.sum(portfolio_values)),
          round(np.sum(portfolio_profits), 2)))
    entry_age = np.arange(n)
    plt.bar(entry_age, portfolio_profits)
    plt.xlabel("Entry age")
    plt.ylabel("Entity's profits")
    print()
    print("To continue please close the bar chart screen")
    plt.show()
    return None
