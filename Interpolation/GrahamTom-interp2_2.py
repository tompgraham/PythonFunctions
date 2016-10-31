#===============================================================================
#                               General Documentation
"""Main module

    See module docstring for description.
"""

#-------------------------------------------------------------------------------
#                               Addition Documentation
#
#
#Modification History
# - Created 10/27/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

import numpy as np
import matplotlib.pyplot as plt

def main():
    """ Module to calculate the unknowns in the mass equation T=Cm^n via linear
    regression
    
    This module contains a main function which defines to arrays which
    constitute the T values and m values in the above equation.  It takes the
    log of both arrays, and then runs them through a linear regression, defined
    by formula 1.19 of Kiusalaas.  It then prints out the solution and
    plots the data along with the regression line.
    """
    
    tValues = np.array([.56, .83, 1.05, 1.28, 1.55, 1.75, 2.22])
    mValues = np.array([.1, .2, .4, .5, .75, 1.0, 1.5])
    
    tValues = np.log(tValues)
    mValues = np.log(mValues)
    
    coef = LinearFit(mValues, tValues)
    
    yValues = np.zeros(len(mValues))
    yValues = coef[1] * mValues + coef[0]
    
    plt.plot(mValues, tValues)
    plt.plot(mValues, yValues)
    plt.xlabel("Mass values")
    plt.ylabel("T values")
    plt.title("Log(T) plotted by Log(m)")
    plt.show()
    
    
    
    print("n = " + str(coef[1]))
    print("C = " + str(np.e ** coef[0]))

def LinearFit(xValues, yValues):
    
    #Calculates the numerator and denominatory for slope calculation
    sumTop = np.sum(yValues[0:] * (xValues[0:] - np.mean(xValues)))
    sumBottom = np.sum(xValues[0:] * (xValues[0:] - np.mean(xValues)))
    
    slope = sumTop/sumBottom
    intercept = np.mean(yValues) - np.mean(xValues) * slope
    
    #Puts coefficients in array to be returned
    coef = np.array([intercept, slope])
    
    return coef;
    
if (__name__ == "__main__"):
    main()