###########################################
# Created by The Machine Shop 2021        #
# Visit our website TheMachineShop.uk     #
# This script interfaces the Zio Qwiic    #
# TOF distance sensor (RFD77402) to a     #
# Raspberry Pi Pico over i2c and converts #
# the data to cm                          #  
###########################################


from machine import Pin,I2C #import some machine libraries
import time, rfd77402 #import some external libraries

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000) #setup the i2c bus
tof = rfd77402.RFD77402(addr=0x4C,i2c=i2c) #setup the tof sensor object
time.sleep(0.1) #small delay, no rush
tof.begin() #start the rof sensor

while True:
    t = 0 #reset the average accumulator
    for i in range(0, 4): #for loop creates an average value over 5 samples
        tof.takeMeasurement() #trigger the measurement
        t = t + tof.getDistance() #collect the measurement and add it to the accumulator
    t = t * 0.2 #divide the accumulator by 5
    print("Distance is: " + str(t) + " cm") #print the value
