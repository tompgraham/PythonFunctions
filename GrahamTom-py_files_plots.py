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
# - Created 10/12/2016 by Tom Graham for CSS 455, University of Washington, 
#   Bothell
#
#Notes:
# - Written for Python 2.7.12
#===============================================================================

import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

def main():
    """ Module to calculate data and graph from text document
    
    This module reads in the text file ASFG_TS.txt and extracts the julian day
    and temperature information placing them into two separate arrays.  This
    module places a mask on any data without a location or temperature.  It then
    prints to the command line the mean, the median, and the standard deviation
    as well as generating a graph of the data with day on the x axis and
    temperature on the y axis.
    """
    
    dataFile = open('ASFG_Ts.txt', 'r')
    dataLine = dataFile.readlines()
    dataFile.close()
    
    #Trims list to usable data
    dataLine.pop(0)
    dataLine.pop(0)
    dataLine.pop(0)
    dataLine.pop(len(dataLine)-1)
    
    arrayOfTemps = ma.masked_array(np.zeros(len(dataLine)), dtype = 'f')
    arrayOfDays = np.zeros(len(dataLine), dtype = 'f')
    
    for i in range (len(dataLine)):
        line = dataLine[i].split('\t')
        arrayOfDays[i] = float(line[0])
        
        #Checks to make sure there are the correct number of data elements
        #as well as making sure temperature has a value, if not, will place
        #default bad value, and mask it
        if (len(line) != 4 or line[3] == "\n"):
            arrayOfTemps[i] = 999999.0
            arrayOfTemps[i] = ma.masked
        else:
            arrayOfTemps[i] = float(line[3])
            
            #Masks the value if there is no value for latitude or longitude
            if (line[1] == "" or line[2] == ""):
                arrayOfTemps[i] = ma.masked  
                  
    meanTemp = ma.mean(arrayOfTemps)
    stdDev = ma.std(arrayOfTemps)
    medTemp = ma.median(arrayOfTemps)
    
    plt.plot(arrayOfDays, arrayOfTemps)
    plt.xlabel('Time by Julian Day')
    plt.ylabel('Temperature in Degrees C')
    plt.title('Surface Temperature Data from SHEBA')
    plt.show()
    
    
    print("Mean temperature = " + str(meanTemp))
    print("Median temperature = " + str(medTemp))
    print("Standard deviation = " + str(stdDev))
        
if (__name__ == "__main__"):
    main()