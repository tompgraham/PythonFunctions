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
# - Created 10/10/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

import numpy as N
import numpy.ma as ma

def slope(ycoord, xcoord): 
    """ Calculate the slopes at given x values
    
    Method Arguments:
        * ycoord: A numpy array of y coordinates
        * xcoord: A numpy array of x coordinates
        
    Output:
        * An array of slopes.  Note that the array is a masked array and
          the edge cases have been masked.
          
    The slopes are calculated by finding the slope of the line between
    each of the given points.  The slope at each point is then taken to be
    the average of the two lines on either side of the point.  The edge cases
    are masked, since we only have the value for the slope on one side of the
    point.
    """
    size = xcoord.size
    
    #Calculates the slope of the lines between the points.
    slopes = ycoord[1:] - ycoord[:(size-1)] / xcoord[1:] - xcoord[:(size-1)]
    
    #Creates a zeroed array
    slopesAtX = N.zeros(size)
    
    #Sets edge values
    slopesAtX[0] = slopes[0]
    
    slopesAtX[size-1] = slopes[slopes.size-1]
    
    #Calculates slopes at given points
    slopesAtX[1:size-1] = (slopes[:slopes.size -1] + slopes[1:])/2
    
    #Creates masked array to return
    slopesToReturn = ma.masked_array(data = slopesAtX)
    
    slopesToReturn[0] = ma.masked
    
    slopesToReturn[size-1] = ma.masked
    
    return slopesToReturn
    
#===============================TEST_MODULE=====================================

#Function for testing, will run if function is called as the main function.
if (__name__ == "__main__"):
    x = N.array([0,1,2,3,4])
    y = N.array([-20.1, -2.9, 1.5, 3.2, -1.3])
    dydx = slope(y,x)
    print (dydx)