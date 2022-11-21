"""
Author: Andreas Brecl
Date: 11/07/2022

This class will handle pulling of the data for astronomy. It will then format
the information into a string to be passed out.
"""

# Import dependencies
import sys
import ephem
from datetime import date

#class GetAstronomyData:
#    def __init__(self) -> None:
#        pass

latitude = '40.0150'
longitude = '-105.2705'
currentDate = '2022/11/20 7:00:00'

denver = ephem.Observer()
denver.lat = latitude
denver.long = longitude
denver.date = currentDate

mars = ephem.Moon()

print(ephem.next_new_moon(currentDate))
#print(ephem.moon_phase(currentDate))
