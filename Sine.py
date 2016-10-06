#===============================================================================
#                               General Documentation
"""Single Function Module

    See function docstring for description.
"""

#-------------------------------------------------------------------------------
#                               Addition Documentation
#
#
#Modification History
# - Created 10/5/2016 by Tom Graham for CSS 455, University of Washington, Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================
import numpy

def sine(value, tol = 1e-8):
    """Calculate the sine of a decimal number
    
    Method Arguments:
    * value:  The value this function will calculate the sine of.  The value
      is a numeric floating point number.
    
    * Tol: The level of precision desired for the sine calculation.  Is a
      percentage of the end result.  I.e. if passed .0001, will calculate the
      answer to a .01% tolerance as the end result converages.  If passed None
      will default to a .0001% tolerance.
    
    Output: 
    * Sine of the value.  Numeric floating point number called 'sum'
      representing the numeric end result of the sine of the initial value. 
    
    The sine is calculated via a series expansion.  Given we can't extend the
    series infinitely, the cut off is determined by the tolerance variable.
    
    """
    
    #- Import Statements:
    
    import math
    
    #- Initialize variables
    
    n = 1
    sumPrev = 0.0
    sum = float(value)
    
    #- Check if value passed is zero
    if (value == 0):
        return 0
    
    #- Calculate the sin of the value using a series expansion
    
    while(abs((sum-sumPrev)/sum) > tol):
        sumPrev = sum
        sum = sum + ((-1)**n)*(value**(2 * n + 1)/math.factorial(2 * n + 1))   
        n = n + 1

    #- Returns sine of the value

    return sum

if (__name__ == "__main__"):
    print 'Numpy module: %.20f' % numpy.sin(3.4)
    print 'This module: %.20f' % sine(3.4)
    

