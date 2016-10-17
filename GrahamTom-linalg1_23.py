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
# - Created 10/16/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements
from gaussElimin import gaussElimin
import numpy as np
from numpy.random import rand

def main(n = 200):
    """ Program to test the gaussElimin function, Kiusalaas, Jaan, Numerical 
    Methods in Engineering with Python 3 pg 41
    
    This program creates a 2D array of size n filled with random values.  
    Default size is 200.  It then creates a b matrix of size n, with values that
    are the sum of the equivalent nth row of the a matrix.  It then runs
    gaussElimin on these two matrixes, with an expected matrix of near 1 x
    values.
    """
    
    a = rand(n,n)
    
    b = np.zeros(n, dtype = 'f')
    
    for i in range(n):
        b[i] = np.sum(a[i])
        
    x = gaussElimin(a,b)
    
    print(x)
    
if (__name__ == "__main__"):
    main()