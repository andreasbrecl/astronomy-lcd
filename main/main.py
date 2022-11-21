#!/usr/bin/env python3

"""
Author: Andreas Brecl
Date: 11/07/2022

This program will pull daily astronomy information and display this information
on an LCD display. It will pull the current moon phase, times planets rise and
set, cloud cover, and moon rise and set time. It will work by running I2C
connection on a raspberry pi.
"""

from lib.get_astronomy_data import GetAstronomyData
from lib.display_on_lcd import DisplayOnLCD
from datetime import date

def main():
    """
    This function will execute the primary functionaily of this program. It will
    run the loop needed to display the information to the LCD.

    Input:  None

    Output: None
    """
    # Define variables for astronomy
    latitude = '40.0150'
    longitude = '-105.2705'

    # Define variables for LCD
    lcdMode = 'i2c'
    cols = 20
    rows = 4
    charmap = 'A00'
    i2cExpander = 'PCF8574'
    address = 0x27 
    port = 1

    # Define run time of LCD
    runTime = 500

    # Create objects
    astronomyData = GetAstronomyData(latitude, longitude)
    displayData = DisplayOnLCD(lcdMode, cols, rows, charmap, i2cExpander, address, port)

    # Run script
    while True:

        # Pull date
        currentDate = getDate()

        # Get planet info
        planetInfo = astronomyData.getPlanetInfo(currentDate)

        # Display information to LCD
        for x in range(runTime):
            displayData.displayMessage(planetInfo)


def getDate():
    """
    
    """
    # Pull date
    todayNoFormat = str(date.today())

    # Format date
    todaySplit = todayNoFormat.split("-")
    today = todaySplit[0] + '/' + todaySplit[1] + '/' + todaySplit[2] + ' 7:00:00'

    return today


if __name__ == "__main__":
    main()