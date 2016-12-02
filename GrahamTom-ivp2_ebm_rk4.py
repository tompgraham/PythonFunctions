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
# - Created 11/30/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements

import numpy as np

def A(T, T_ice = 273, T_no_ice = 293):
    """Linear function to determine the value of A(T)
    """
    
    if (T <= T_ice):
        return 1.0
    elif (T >= T_no_ice):
        return 0.0
    else:
        return -.05 * T + 14.65
    
def engBalModel(T):
    """Function to determine value of T, based upon previous temperature
    """
    S = 342.5
    epsilon_tau_a = .62
    sigma = 5.67e-8
    pC = 2.06e8

    return (S * (1-A(T)) - epsilon_tau_a * sigma * T ** 4) / pC

def integrate(F,y,h, numIter):
    """Runge-Kutta method taken from Numerical Methods in Engineering,
       Jaan Kiusalaas
    """
    def run_kut4(F,y,h):
        # Computes increment of y from Eqs. (7.10)
        K0 = h*F(y)
        K1 = h*F(y + K0/2.0)
        K2 = h*F(y + K1/2.0)
        K3 = h*F(y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    Y = []
    Y.append(y)
    for i in range(numIter):
        y = y + run_kut4(F,y,h)
        Y.append(y)
    return np.array(Y)
    
def main():
    """Main function
    """
    print (integrate(engBalModel,274, 86400, 3000))
    
if (__name__ == "__main__"):
    main()