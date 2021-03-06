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
import matplotlib.pyplot as plt

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

def Euler(df, yinit, h, nsteps):
    """Euler's method function
    """
    y = [yinit]
    for i in range(nsteps):
        x = i*h
        ynew = y[i-1] + df(y[i-1]) * h
        y.append(ynew)
        
    return y
    
def main():
    """Main function
    """
    temps = (Euler(engBalModel,286, 86400, 4000))
    plt.plot(temps)
    plt.xlabel('time')
    plt.ylabel('Temperature in Degrees K')
    plt.title('Temperature approaching equilibrium')
    plt.show()
    
if (__name__ == "__main__"):
    main()