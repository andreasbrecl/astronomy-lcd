"""
Author: Andreas Brecl
Date: 11/07/2022

This class will handle pulling of the data for astronomy. It will then format
the information into a string to be passed out.
"""

# Import dependencies
import sys
import ephem

class GetAstronomyData:
    def __init__(self, latitude, longitude):
        """
        
        """
        # Define class variables
        self.latitude = latitude
        self.longitdue = longitude

        # Define location information
        location = ephem.Observer()
        location.lat = latitude
        location.long = longitude


        # Define location class object
        self.location = location


    def convertToMST(self, riseTime, setTime):
        """
        
        """
        # Convert to MST from UTC
        riseTimeSplit = riseTime.split(":")
        setTimeSplit = setTime.split(":")

        # Pull hour
        riseTimeHour = riseTimeSplit[0]
        setTimeHour = setTimeSplit[0]

        # Convert to integer
        riseTimeHourInt = int(riseTimeHour)
        setTimeHourInt = int(setTimeHour)

        # Set to UTC
        riseTimeHourMST = riseTimeHourInt - 7
        setTimeHourMST = setTimeHourInt - 7

        # Adjust for negatives
        if riseTimeHourMST < 0:
            riseTimeHourMST = riseTimeHourMST + 24

        if setTimeHourMST < 0:
            setTimeHourMST =  setTimeHourMST + 24

        # Recombine
        riseTime = str(riseTimeHourMST) + ":" + riseTimeSplit[1]
        setTime = str(setTimeHourMST) + ":" + setTimeSplit[1]

        return riseTime, setTime
        

    def getRiseAndSetTimes(self, celestialObject):
        """
        
        """
        # Pull rise and set information
        riseTimeAndDate = str(self.location.next_rising(celestialObject))
        setTimeAndDate = str(self.location.next_setting(celestialObject))
        
        # Split data
        riseTimeAndDateSplit = riseTimeAndDate.split()
        setTimeAndDateSplit = setTimeAndDate.split()

        # Pull time
        riseTime = riseTimeAndDateSplit[1]
        setTime = setTimeAndDateSplit[1]

        # Convert to MST from UTC
        riseTime, setTime = self.convertToMST(riseTime, setTime)

        return riseTime, setTime

    def getMarsInfo(self):
        """
        
        """
        # Get rise and set time information
        mars = ephem.Mars()
        riseTimeMars, setTimeMars = self.getRiseAndSetTimes(mars)

        return riseTimeMars, setTimeMars

    def getSaturnInfo(self):
        """
        
        """
        # Get rise and set time information
        saturn = ephem.Saturn()
        riseTimeSaturn, setTimeSaturn = self.getRiseAndSetTimes(saturn)

        return riseTimeSaturn, setTimeSaturn

    def getJupiterInfo(self):
        """
        
        """
        # Get rise and set time information
        jupiter = ephem.Jupiter()
        riseTimeJupiter, setTimeJupiter = self.getRiseAndSetTimes(jupiter)

        return riseTimeJupiter, setTimeJupiter

    def getVenusInfo(self):
        """
        
        """
        # Get rise and set time information
        venus = ephem.Venus()
        riseTimeVenus, setTimeVenus = self.getRiseAndSetTimes(venus)

        return riseTimeVenus, setTimeVenus

    def getMoonInfo(self):
        """
        
        """
        # Get rise and set time information
        moon = ephem.Moon()
        riseTimeMoon, setTimeMoon = self.getRiseAndSetTimes(moon)

        # Get New moon information
        nextNewMoonDateAndTime = str(ephem.next_new_moon(self.location.date))
        nextNewMoonDateAndTimeSplit = nextNewMoonDateAndTime.split(" ")
        nextNewMoonDate = nextNewMoonDateAndTimeSplit[0]

        # Get full moon information
        nextFullMoonDateAndTime = str(ephem.next_full_moon(self.location.date))
        nextFullMoonDateAndTimeSplit = nextFullMoonDateAndTime.split(" ")
        nextFullMoonDate = nextFullMoonDateAndTimeSplit[0]


        return riseTimeMoon, setTimeMoon, nextNewMoonDate, nextFullMoonDate

    def getSunInfo(self):
        """
        
        """
        # Get rise and set time information
        sun = ephem.Sun()
        riseTimeSun, setTimeSun = self.getRiseAndSetTimes(sun)

        return riseTimeSun, setTimeSun

    def getPlanetInfo(self, currentDate):
        """
        """
        # Set date
        self.location.date = currentDate

        # Pull planet information
        riseTimeMars, setTimeMars = self.getMarsInfo()
        riseTimeSaturn, setTimeSaturn = self.getSaturnInfo()
        riseTimeJupiter, setTimeJupiter = self.getJupiterInfo()
        riseTimeVenus, setTimeVenus = self.getVenusInfo()
        riseTimeMoon, setTimeMoon, nextNewMoonDate, nextFullMoonDate = self.getMoonInfo()
        riseTimeSun, setTimeSun = self.getSunInfo()

        # Return list
        planetInfo = [riseTimeMars, setTimeMars, riseTimeSaturn, setTimeSaturn, riseTimeJupiter, setTimeJupiter, riseTimeVenus, setTimeVenus, riseTimeMoon, setTimeMoon, riseTimeSun, setTimeSun, nextNewMoonDate, nextFullMoonDate]
        return planetInfo
