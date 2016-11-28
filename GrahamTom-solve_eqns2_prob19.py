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
# - Created 11/16/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements

import numpy as np
    
def main():
    """Module to calculate the moment a rocket hits the speed of sound
    
    This module calculates the moment a rocket hits the speeds of sound.  It
    takes the function to determine the velocity and the derivative of that
    function in respect to time and passes them into a newtonRaphson function
    taken from Numerical Methods in Egnineering with Python 3, by Jaan
    Kiusalaas.
    """
    
    u = 2510
    M0 = 2.8 * 1.e6
    rn = 13.3 * 1.e3
    g = 9.81
    t = 0
    vTarget = 335
    
    time = newtonRaphson( lambda _:f(_,u,M0,rn,g,vTarget),lambda _:df(_,u,M0,rn,g), 0.0,100)
    print(str(time))
    
def f(t,u,M0,rn,g,vTarget): 
    return u * np.log(M0 / (M0 - rn * t)) - g * t - vTarget

def df(t,u,M0,rn,g):
    return (u * rn) / (M0 - rn * t) - g
  
def newtonRaphson(f,df,a,b,tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa*fb > 0.0: print("Root is not bracketed")
    x = 0.5*(a + b)
    for i in range(30):
        fx = f(x)
        if abs(fx) < tol: return x
        # Tighten the brackets on the root
        if fa*fx < 0.0:
            b=x
        else:
            a=x
        # Try a Newton-Raphson step
        dfx = df(x)
        # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
        # If the result is outside the brackets, use bisection
        if (b - x)*(x - a) < 0.0:
            dx = 0.5*(b-a)
            x = a + dx
        # Check for convergence
        if abs(dx) < tol*max(abs(b),1.0): return x
        print "Too many iterations in Newton-Raphson"



if __name__ == "__main__":
    main()