###########################################
# Created by The Machine Shop 2019        #
# Visit our website TheMachineShop.uk     #
# This script interfaces the Zio QWIIC    #
# Temperature and Humidity sensor (SHT31) #
# to a Raspberry Pi Pico over i2c and     #
# converts the data to Celsius and        #
# percentage to print to the terminal and #
# an OLED display                         #
###########################################

# import the required libraries

from machine import I2C, Pin
import time
from ssd1306 import SSD1306_I2C

# Start the i2c bus and label as 'i2c'
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
# Setup the OLED
oled = SSD1306_I2C(128, 32, i2c, addr=0x3c)

# Setup a while loop to continuously take measurements
while True:
    # Send the start conversion command to the SHT31
    i2c.writeto(0x44, bytes([0x2C, 0x06]))

    # wait for the conversion to complete
    time.sleep(0.5)

    # Read the data from the SHT31 containing
    # the temperature (16-bits + CRC) and humidity (16bits + crc)
    data = i2c.readfrom_mem(0x44, 0x00, 6)

    # Convert the data
    temp = data[0] * 256 + data[1]
    cTemp = -45 + (175 * temp / 65535.0)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

    # Output data to the terminal
    print("Temperature in Celsius is : %.2fC" % cTemp)
    print("Relative Humidity is : %.2f %%RH" % humidity)

    # print the data to the OLED display
    oled.fill(0)
    oled.text("Temp:" + ("%.2f" % cTemp) + 'C', 20, 8)
    oled.text("Humid:" + ("%.2f" % humidity) + '%', 16, 24)
    oled.show()
