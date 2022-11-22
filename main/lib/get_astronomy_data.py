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
        This constructor defines the information for astronomy objects needed
        for calculating rise/set/phases.

        Input:  latitude <str> - Latitude of observer
                longitude <str> - Longitude of observer

        Output: None
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
        This converts the rise/set time to MST from UTC.

        Input:  riseTime <str> - Rise time UTC
                setTime <str> - Set time UTC

        Output: riseTime <str> - Converted rise time
                setTime <str> - Converted set time
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
        Calculates the rise and set time based on the object inputted into
        the system. This will change per day.

        Input:  celestialObject <obj> - pyephem object for celestial body

        Output: riseTime <str> - Rise time of object
                setTime <str> - Set time of object
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
        This function pulls the rise and set information for Mars.

        Input:  None

        Output: riseTimeMars <str> - Rise time for Mars
                setTimeMars <str> - Set time for Mars
        """
        # Get rise and set time information
        mars = ephem.Mars()
        riseTimeMars, setTimeMars = self.getRiseAndSetTimes(mars)

        return riseTimeMars, setTimeMars

    def getSaturnInfo(self):
        """
        This function pulls the rise and set information for Saturn.

        Input:  None

        Output: riseTimeSaturn <str> - Rise time for Saturn
                setTimeSaturn <str> - Set time for Saturn
        """
        # Get rise and set time information
        saturn = ephem.Saturn()
        riseTimeSaturn, setTimeSaturn = self.getRiseAndSetTimes(saturn)

        return riseTimeSaturn, setTimeSaturn

    def getJupiterInfo(self):
        """
        This function pulls the rise and set information for Jupiter.

        Input:  None

        Output: riseTimeJupiter <str> - Rise time for Jupiter
                setTimeJupiter <str> - Set time for Jupiter
        """
        # Get rise and set time information
        jupiter = ephem.Jupiter()
        riseTimeJupiter, setTimeJupiter = self.getRiseAndSetTimes(jupiter)

        return riseTimeJupiter, setTimeJupiter

    def getVenusInfo(self):
        """
        This function pulls the rise and set information for Venus.

        Input:  None

        Output: riseTimeVenus <str> - Rise time for Venus
                setTimeVenus <str> - Set time for Venus
        """
        # Get rise and set time information
        venus = ephem.Venus()
        riseTimeVenus, setTimeVenus = self.getRiseAndSetTimes(venus)

        return riseTimeVenus, setTimeVenus

    def getMoonInfo(self):
        """
        This function pulls the rise and set information for Moon.

        Input:  None

        Output: riseTimeMoon <str> - Rise time for Moon
                setTimeMoon <str> - Set time for Moon
                nextNewMoonDate <str> - New moon future date
                nextFullMoonDate <str> - Full moon future date
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
        This function pulls the rise and set information for Sun.

        Input:  None

        Output: riseTimeSun <str> - Rise time for Sun
                setTimeSun <str> - Set time for Sun
        """
        # Get rise and set time information
        sun = ephem.Sun()
        riseTimeSun, setTimeSun = self.getRiseAndSetTimes(sun)

        return riseTimeSun, setTimeSun

    def getPlanetInfo(self, currentDate):
        """
        This function pulls all the information for the celestial bodies.

        Input:  currentDate <str> - Date of today

        Output: planetInfo <list> <str> - This is a list of the planet information for rise/set/phases
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
