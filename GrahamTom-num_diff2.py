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
# - Created 11/22/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

#import statements

import numpy as np

def main():
    """Module to calculate the speed and angle of an airplane
    
    This module calculates the speed and angle of an airplane based upon two
    sets of angles taken from two radar station over of a period of time.  It
    uses a difference approximation to find the slopes and calculates the
    velocity vector given by Kiusalaas in Numerical Methods in Engineering with
    Python 3.
    """
    alphaAngles = np.array([54.80, 54.06, 53.34])
    betaAngles = np.array([65.59, 64.59, 63.62])
    
    alphaAngles = alphaAngles * np.pi / 180.0
    betaAngles = betaAngles * np.pi / 180.0
    
    deltaT = 1
    a = 500
    
    alphaDer = diffApprox(alphaAngles, deltaT)
    betaDer = diffApprox(betaAngles, deltaT)
    
    #calculates the x component of the velocity vector
    vectorX = (a * (alphaDer[1]*np.sin(betaAngles[1])*np.cos(betaAngles[1]) - 
    betaDer[1] * np.sin(alphaAngles[1])*np.cos(alphaAngles[1]))) / (np.sin(alphaAngles[1]-betaAngles[1])**2)
    
    #calculates the y component of the velocity vector
    vectorY = (a * (alphaDer[1] * np.sin(betaAngles[1]) ** 2 - betaDer[1] * 
    np.sin(alphaAngles[1]) ** 2)) / np.sin(alphaAngles[1]-betaAngles[1]) ** 2
    
    #gets speed from velocity vector
    speed = np.sqrt(vectorX ** 2 + vectorY ** 2)
    
    #gets angle of inclination
    angle = vectorY / vectorX * 180 / np.pi
    
    print("Speed =" + str(speed))
    print("angle =" + str(angle))
    

def diffApprox(values, deltaT):
    """Function to calculate the derivative at a diven DeltaT from a set of
    values using a difference approximation
    """
        
    n = len(values)
        
    diffValues = []
    
    #If left position uses a forward difference approximation    
    diffValues.append(-3 * values[0] + 4 * values[1] - values[2] / 
    (2 * deltaT))
    
    #For middle values uses a central difference approximation
    for i in range (1, n-1):
        diffValues.append(( -values[i-1] + values[i+1] ) / (2 * deltaT))
    
    #For the right value uses a backward difference approximation
    diffValues.append((values[n-2] -4 * values[i-1] + 3 * values[i]) /
    (2 * deltaT))
    
    return diffValues
    
if __name__ == "__main__":
    main()