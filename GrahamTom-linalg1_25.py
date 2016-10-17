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

import numpy as np
from gaussElimin import gaussElimin

def main(m = np.array([10.0, 4.0, 5.0, 6.0]), u = np.array([.23, .3, .2]), 
thetaDeg = 45.0, g=9.82):
    """ Program to find tensile forces and tension represetned as T1,T2,T3
    and Acceleration, A. From Kiusalaas, Jaan, Numerical Methods in Engineering 
    with Python 3 Pg 41, 58-59, 
    
    This program takes two arrays, and two floats.  The m array represents
    the masses of the object, the u array represents the coefficient of
    friction, the thetadDeg is the degree of angle, and g is the constant m/s^2.
    It uses the equations on pg 59 to derive two matrices and solve the
    equations using the gaussElimin function from pg 41.
    """
    
    #Transform degrees to radians      
    theta = thetaDeg * np.pi / 180.0
    
    #Build vector b
    b = np.array((m[:3] * g * (np.sin(theta) - u * np.cos(theta))) + m[3] * g, 
    dtype = 'f')
    
    #Build matrix a
    a = np.array([[1.0, 0.0, m[0.0]/m[3.0]], [-1.0, 1.0, m[1.0]/m[3.0]], 
    [0.0, -1.0, 1.0 + m[2.0]/m[3.0]]], dtype = 'f')
    
    x = gaussElimin(a,b)
    
    #Calculate acceleration
    aVal = -g + x[2]/m[3]
    
    print("T1 = " + str(x[0])) 
    print("T2 = " + str(x[1]))
    print("T3 = " + str(x[2]))
    print("A = " + str(aVal))
    
if (__name__ == "__main__"):
    main()