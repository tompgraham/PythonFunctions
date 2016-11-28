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
# - Created 11/27/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements


import numpy as np

def f(z,r): 
    """Function representing the bending rigity of a beam
    """
    return (z ** 2 * np.sqrt(1 + (r * z) ** 2))

def computeCofHB(hb, useTrap = False, tol=1.e-5, maxNodes=100):
    """Function to determine the value of C(h/b)
    
    This module uses the rigity function and runs it through the Gauss
    quadrature successively to determine the value of C(h/b) for any value
    of h/b.  It return both the value, and the number of passes required
    to reach an answer within the given tolerance.  Also takes a boolean that
    if passed true, will perform the calculation using the composite trapezoidal
    rule instead.
    """
    a = 0
    b = 1
    if(not useTrap):
        oldVal = gaussQuad( lambda _ : f(_, hb), a, b, 2)
        for i in range(3, maxNodes + 1):
            newVal = gaussQuad( lambda _ : f(_,hb), a, b, i)
            if (abs(newVal - oldVal) < tol):
                return newVal, i
            oldVal = newVal
    else:
        oldVal = trapezoid(lambda _ : f(_, hb), a, b, 2)
        for i in range(3, maxNodes + 1):
            newVal = trapezoid(lambda _ : f(_, hb), a, b, i)
            if (abs(newVal-oldVal) < tol * max(abs(newVal),1.0)):
                return newVal, i
            oldVal = newVal
            
def gaussNodes(m,tol=10e-9):
    """Helper module for Gauss quadrature taken from Numerical Methods in 
    Engineering with Python 3, by Jaan Kiusalaas
    """
    def legendre(t,m):
        p0 = 1.0; p1 = t
        for k in range(1,m):
            p = ((2.0*k + 1.0)*t*p1 - k*p0)/(1.0 + k )
            p0 = p1; p1 = p
        dp = m*(p0 - t*p1)/(1.0 - t**2)
        return p,dp
        
    A = np.zeros(m)
    x = np.zeros(m)
    nRoots = (m + 1)/2 # Number of non-neg. roots
    for i in range(nRoots):
        t = np.cos(np.pi*(i + 0.75)/(m + 0.5)) # Approx. root
        for j in range(30):
            p,dp = legendre(t,m) # Newton-Raphson
            dt = -p/dp; t = t + dt # method
            if abs(dt) < tol:
                x[i] = t; x[m-i-1] = -t
                A[i] = 2.0/(1.0 - t**2)/(dp**2) # Eq.(6.25)
                A[m-i-1] = A[i]
                break
    return x,A
    
def gaussQuad(f,a,b,m):
    """Module for Gauss quadrature taken from Numerical Methods in Engineering 
    with Python 3, by Jaan Kiusalaas
    """
    c1 = (b + a)/2.0
    c2 = (b - a)/2.0
    x,A = gaussNodes(m)
    sum = 0.0
    for i in range(len(x)):
        sum = sum + A[i]*f(c1 + c2*x[i])
    return c2*sum

def trapezoid(f,a,b,k):
    """Function to perform the composite trapezoidal rule
    """
    h = (b-a)/float(k)
    total = f(a) + f(b)
    for i in range(1, k):
        total = total + 2.0 * f(a + i * h)
    return total * h / 2.0

if __name__ == '__main__':
    """Test method
    Runs three values from computeCoOFHB using both Gauss Quadrature and the
    composite trapezoidal rule to compare how many passes the respective
    functions take to reach an answer within the tolerance
    """
    print(computeCofHB(.5))
    print(computeCofHB(1.0))
    print(computeCofHB(2.0))
    
    print(computeCofHB(.5, True))
    print(computeCofHB(1.0, True))
    print(computeCofHB(2.0, True))
    
#Note re accuracy: Gauss-Legendre quardrature appears to be more accurate than
#the trapezoidal rule, given it takes a significantly larger number of panels
#than the quadrature does nodes