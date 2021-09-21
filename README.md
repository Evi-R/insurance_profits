# Project name 
Calculation of company profits for German private health insurance contracts. 
***
## Table of Contents
1. [General Info](#general-info)
2. [Project status and further steps](#project-status-and-further-steps)
3. [Technologies](#technologies)
4. [Usage](#usage)

***
## General Info
### Goal 
The goal is the IFRS 17 valuation of contracts in German private health insurance. 
The original computation was performed for a university project that involved the first applications of Python. 

### Project structure
The calculations are based on 2-dimensional numpy arrays, where the first dimension shows the age at entry and the second shows the progression over time. 
* The first part calculates the discounted profits for all possible entry ages and stores the result. 
* The second part calculates the portfolio profits. 
***
## Project status and further steps
### Current status
The project calculates future company profits: 
* for one contract, for contract period not exceeding 5 years, 
* using real actuarial formulas, 
* for a portfolio containing an arbitrary number of insured persons with arbitrary entry ages.

### Further steps
* Replace the current for-loops with clever matrix multiplications.
* Check if ”Pandas” would be a better tool for these calculations.
* Add medical inflation, which triggers regular premium adjustments.
* Add further features of health insurance contracts, such as costs, allocation of pregnancy costs to both genders, risk surcharge, surcharge for financing the basic tariff a.o.
* Process different contracts with different input values.
* Enable distinction between actual and expected values.
* Include tests and error messages.
* Replace the fixed interest rate with the simulation of the financial market.
* Calculate with real actuarial values and real portfolios. 
***
## Technologies
* [Python](https://www.python.org): Version 3.9.0 
* [NumPy](https://numpy.org/): Version 1.20.1
* [Matplotlib](https://matplotlib.org): Version 3.4.3
***
## Usage
* Install numpy and matplotlib. 
* Run main module. The code asks in the console 
  * if the input data should be updated (answer with "yes" or "no") and 
  * which portfolio should be selected (answer with "1", "2" or "3"). 
* The input data in "input values" and "portfolio values" as well as their number can be changed. It is important that the number of entries is the same in all input files. 
* The file "insurance_profits_python_test.xlsx contains an Excel calculation of all values and can be used as a test as long as the values do not become too complicated. 
***

