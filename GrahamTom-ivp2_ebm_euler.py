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
# - Created 10/30/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements

def A(T, T_ice = 273, T_no_ice = 293):
    """Linear function to determine the value of A(T)
    """
    
    if (T <= T_ice):
        return 1.0
    elif (T >= T_no_ice):
        return 0.0
    else:
        return -.05 * T + 14.65
    
def engBalModel(f, T, delta_t):
    """Function to determine value of T, based upon previous temperature
    """
    return (342.5*(1-f(T)) - .62 * 5.67e-8 * T ** 4) * delta_t / 2.06e8

def Euler(df, yinit, h, nsteps):
    """Euler's method function
    """
    y = [yinit]
    for i in range(nsteps):
        x = i*h
        ynew = y[i-1] + df(A,y[i-1],x)
        y.append(ynew)
        
    return y
    
def main():
    """Main function
    """
    print (Euler(engBalModel,15, 86400, 12000))
    
if (__name__ == "__main__"):
    main()