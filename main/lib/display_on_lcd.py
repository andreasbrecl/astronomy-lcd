"""
Author: Andreas Brecl
Date: 11/07/2022

This class will handle with displaying information on the LCD screen
via I2C connection. It will take in an input of the message needing
to be displayed.
"""

from RPLCD import i2c
from time import sleep

class DisplayOnLCD:
    def __init__(self, lcdMode, cols, rows, charmap, i2cExpander, address, port):
        """
        This constructor creates the objects for the class. It takes
        in the information needed to establish the i2c communication
        for the LCD.

        Input:  lcdMode <str> - Defines communication protocal
                cols <int> - Number of columns on the LCD
                rows <int> - Number of rows on the LCD
                charmap <str> - Character mapping for LCD
                i2cExpander <str> - i2c expander information
                address <hex> - Hex address for i2c comms
                port <int> - raspberry pi port number

        Output: None
        """
        # Define object variables
        self.lcdMode = lcdMode
        self.cols = cols
        self.rows = rows
        self.charmap = charmap
        self.i2cExpander = i2cExpander
        self.address = address
        self.port = port

        self.lcd = i2c.CharLCD(i2cExpander, address, port=port, charmap=charmap, cols=cols, rows=rows)


    def displayMessage(self, planetInfo):
        """
        This function takes in the planet information as list and
        then displays the information on the LCD screen.

        Input:  planetInfo <list> <str> - This is a list of the planet information for rise/set/phases

        Output: None
        """
        # Define variables
        riseTimeMars = planetInfo[0]
        setTimeMars = planetInfo[1]
        riseTimeSaturn = planetInfo[2]
        setTimeSaturn = planetInfo[3]
        riseTimeJupiter = planetInfo[4]
        setTimeJupiter = planetInfo[5]
        riseTimeVenus = planetInfo[6]
        setTimeVenus = planetInfo[7]
        riseTimeMoon = planetInfo[8]
        setTimeMoon = planetInfo[9]
        riseTimeSun = planetInfo[10]
        setTimeSun = planetInfo[11]
        nextNewMoonDate = planetInfo[12]
        nextFullMoonDate = planetInfo[13]

        # Turn on backlight
        self.lcd.backlight_enabled = True

        # Display information mars
        riseTimeMarsString = "Mars Rise: " + str(riseTimeMars)
        setTimeMarsString = "Mars Set: " + str(setTimeMars)
        self.lcd.write_string(riseTimeMarsString)
        self.lcd.crlf()
        self.lcd.write_string(setTimeMarsString)
        self.lcd.crlf()

        # Display information saturn
        riseTimeSaturnString = "Saturn Rise: " + str(riseTimeSaturn)
        setTimeSaturnString = "Saturn Set: " + str(setTimeSaturn)
        self.lcd.write_string(riseTimeSaturnString)
        self.lcd.crlf()
        self.lcd.write_string(setTimeSaturnString)

        # Sleep between
        sleep(10)
        self.lcd.close(clear=True)

        # Display information jupiter
        riseTimeJupiterString = "Jupiter Rise: " + str(riseTimeJupiter)
        setTimeJupiterString = "Jupiter Set: " + str(setTimeJupiter)
        self.lcd.write_string(riseTimeJupiterString)
        self.lcd.crlf()
        self.lcd.write_string(setTimeJupiterString)
        self.lcd.crlf()

        # Display information venus
        riseTimeVenusString = "Venus Rise: " + str(riseTimeVenus)
        setTimeVenusString = "Venus Set: " + str(setTimeVenus)
        self.lcd.write_string(riseTimeVenusString)
        self.lcd.crlf()
        self.lcd.write_string(setTimeVenusString)

        # Sleep between
        sleep(10)
        self.lcd.close(clear=True)

        # Display information Moon
        riseTimeJupiterString = "Moon Rise: " + str(riseTimeMoon)
        setTimeJupiterString = "Moon Set: " + str(setTimeMoon)
        self.lcd.write_string(riseTimeJupiterString)
        self.lcd.crlf()
        self.lcd.write_string(setTimeJupiterString)
        self.lcd.crlf()

        # Display information sun
        riseTimeSunString = "Sun Rise: " + str(riseTimeSun)
        setTimeSunString = "Sun Set: " + str(setTimeSun)
        self.lcd.write_string(riseTimeSunString)
        self.lcd.crlf()
        self.lcd.write_string(setTimeSunString)

        # Sleep between
        sleep(10)
        self.lcd.close(clear=True)

        # Display information full and new moon
        newMoonString = "Next New Moon: " 
        newMoonStringDate = str(nextNewMoonDate)
        fullMoonSunString = "Next Full Moon: " 
        fullMoonSunStringDate = str(nextFullMoonDate)
        self.lcd.write_string(newMoonString)
        self.lcd.crlf()
        self.lcd.write_string(newMoonStringDate)
        self.lcd.crlf()
        self.lcd.write_string(fullMoonSunString)
        self.lcd.crlf()
        self.lcd.write_string(fullMoonSunStringDate)
        

        # Sleep between
        sleep(10)
        self.lcd.close(clear=True)

                

