from machine import Pin,I2C
import time, rfd77402
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled = SSD1306_I2C(128, 32, i2c, addr=0x3c)
tof = rfd77402.RFD77402(addr=0x4C,i2c=i2c)
time.sleep(0.1)
tof.begin()

while True:
    t = 0
    for i in range(0, 4):
        tof.takeMeasurement()
        t = t + tof.getDistance()
    t = t * 0.2
    oled.fill(0)
    oled.text("Distance is:", 0, 0)
    oled.text(str(int(t * 0.1)) + " cm", 0, 10)
    oled.text(str(int(t * 0.03937)) + " inch", 0, 20)
    oled.show()
