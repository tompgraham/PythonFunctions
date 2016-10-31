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
from gaussElimin import *

def main():
    """ Module to find a linear and quadratic least squares fit for the given
    data
    
    This module contains a main function which defines to arrays which
    constitute the x values and y values.  They are fed into a PolyFit equation
    defined in Kiusalaas and plotted
    """
    
    xValues = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
    yValues = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])

    yLinValues = np.zeros(len(xValues))
    yQuadValues = np.zeros(len(xValues))
    
    linCoef = PolyFit(xValues, yValues, 1)
    quadCoef = PolyFit(xValues, yValues, 2)
    
    print(linCoef)
    print(quadCoef)
    
    yLinValues = linCoef[0] + xValues * linCoef[1]
    yQuadValues = quadCoef[0] + xValues * quadCoef[1] + xValues**2 * quadCoef[2]
    
    plt.plot(xValues, yValues, "o")
    plt.plot(xValues, yLinValues)
    plt.plot(xValues, yQuadValues)
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.title("Data With a Linear and Quadratic Regression")
    plt.show()
    
    
def PolyFit(xData, yData, m):
    a = np.zeros((m+1, m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp * xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp * temp * xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i,j] = s[i+j]
    return gaussElimin(a,b)  
    
if (__name__ == "__main__"):
    main()