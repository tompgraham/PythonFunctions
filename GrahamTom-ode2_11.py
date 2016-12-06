# -*- coding: utf-8 -*-
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
# - Created 12/5/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements
import numpy as np

def initCond(u):
    conditions = np.array([1.0,u])
    return conditions


def F(x,y):
    F = np.zeros(len(y))
    F[0] = y[1]
    F[1] = -y[1]/x - y[0]
    return F
    
def integrate(F,x,y,xStop,h,tol=1.0e-6):
    """Runge-Kutta method taken from Numerical Methods in Engineering,
       Jaan Kiusalaas
    """
    def run_kut5(F,x,y,h):
        # Runge--Kutta-Fehlberg formulas
        C = np.array([37./378, 0., 250./621, 125./594, \
        0., 512./1771])
        D = np.array([2825./27648, 0., 18575./48384, \
        13525./55296, 277./14336, 1./4])
        n = len(y)
        K = np.zeros((6,n))
        K[0] = h*F(x,y)
        K[1] = h*F(x + 1./5*h, y + 1./5*K[0])
        K[2] = h*F(x + 3./10*h, y + 3./40*K[0] + 9./40*K[1])
        K[3] = h*F(x + 3./5*h, y + 3./10*K[0]- 9./10*K[1] \
        + 6./5*K[2])
        K[4] = h*F(x + h, y - 11./54*K[0] + 5./2*K[1] \
        - 70./27*K[2] + 35./27*K[3])
        K[5] = h*F(x + 7./8*h, y + 1631./55296*K[0] \
        + 175./512*K[1] + 575./13824*K[2] \
        + 44275./110592*K[3] + 253./4096*K[4])
        # Initialize arrays {dy} and {E}
        E = np.zeros(n)
        dy = np.zeros(n)
        # Compute solution increment {dy} and per-step error {E}
        for i in range(6):
            dy = dy + C[i]*K[i]
            E = E + (C[i] - D[i])*K[i]
        # Compute RMS error e
        e = np.sqrt(sum(E**2)/n)
        return dy,e
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    stopper = 0 # Integration stopper(0 = off, 1 = on)
    
    for i in range(10000):
        dy,e = run_kut5(F,x,y,h)
        # Accept integration step if error e is within tolerance
        if e <= tol:
            y = y + dy
            x=x+h
            X.append(x)
            Y.append(y)
            # Stop if end of integration range is reached
            if stopper == 1: break
    # Compute next step size from Eq. (7.24)
    if e != 0.0:
        hNext = 0.9*h*(tol/e)**0.2
    else: hNext = h
    # Check if next step is the last one; is so, adjust h
    if (h > 0.0) == ((x + hNext) >= xStop):
        hNext = xStop - x
        stopper = 1
    h = hNext
    return np.array(X),np.array(Y)
        
    
def ridder(f,a,b,tol=1.0e-9):
    """Ridder method taken from Numerical Methods in Engineering,
       Jaan Kiusalaas
    """
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    for i in range(30):
        # Compute the improved root x from Ridder’s formula
        c = 0.5*(a + b); fc = f(c)
        s = np.sqrt(fc**2 - fa*fb)
        if s == 0.0: return None
        dx = (c - a)*fc/s
        if (fa - fb) < 0.0: dx = -dx
        x = c + dx; fx = f(x)
        # Test for convergence
        if i > 0:
            if abs(x - xOld) < tol*max(abs(x),1.0): return x
        xOld = x
        # Re-bracket the root as tightly as possible
        if fc*fx > 0.0:
            if fa*fx < 0.0: b = x; fb = fx
            else: a = x; fa = fx
        else:
            a = c; b = x; fa = fc; fb = fx
    return None
    print ("Too many iterations")

def main():
    def r(u):
        X,Y = integrate(F,xStart, initCond(u), xStop, h)
        y = Y[len(Y) -1]
        r = y[1]
        return r

    xStart = .01
    xStop = 2.0
    u1 = -100.0
    u2 = 0.0
    h = 0.1
    u = ridder(r,u1,u2)
    X,Y = integrate(F, xStart, initCond(u), xStop, h)
    print(X,Y)
    
if (__name__ == "__main__"):
    main()