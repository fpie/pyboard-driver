""" Scan the OneWire master for devices

	See PybStick-UniPi interface @ MCHobby
	https://shop.mchobby.be/fr/nouveaute/1891-carte-interface-unipi-pro-et-lite-pour-pybstick-3232100018914.html

	See project https://github.com/mchobby/pyboard-driver/tree/master/UniPi-MicroPython-Automation

	domeu, 06 june 2020, Initial Writing (shop.mchobby.be)
	----------------------------------------------------------------------------

	MCHobby invest time and ressource in developping project and libraries.
	It is a long and tedious work developed with Open-Source mind and freely available.
	IF you like our work THEN help us by buying your product at MCHobby (shop.mchobby.be).

	----------------------------------------------------------------------------
	Copyright (C) 2020  - Meurisse D. (shop.mchobby.be)

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
#from unipi import unipi
from machine import I2C
i2c = I2C(2)
import time

from ds2482 import DS2482
oneWire = DS2482( i2c )

print( "Checking for I2C devices...:" )
oneWire.check_presence()

def printAddress( deviceAddress ): # uint8_t deviceAddress[8]
	print( "print address... ")
	#Serial.print("{ ");
	#for (uint8_t i = 0; i < 8; i++)
	#{
	#	// zero pad the address if necessary
	#	Serial.print("0x");
	#	if (deviceAddress[i] < 16) Serial.print("0");
	#	Serial.print(deviceAddress[i], HEX);
	#	if (i<7) Serial.print(", ");
	#}
	#Serial.print(" }");

while True:
	oneWire.device_reset() # Reset the ds2482

	print( "Checking for 1-Wire devices..." )
	if oneWire.wire_reset():
		print( "Devices present on 1-Wire bus" )

		#uint8_t currAddress[8];

		print( "Searching 1-Wire bus..." )

		currAddress = oneWire.wire_search( currAddress )
		while currAddress:
			print( "Found device: " )
			printAddress( currAddress )

		oneWire.wire_reset_search()
	else:
		print( "No devices on 1-Wire bus" )

	time.sleep(5)
