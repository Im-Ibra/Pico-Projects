from machine import Pin
import time

led = Pin(0, Pin.OUT)
sensor = Pin(28, Pin.IN)
 
while True:
    if sensor.value() == 1:
        led.value(1)
    else:
        led.value(0)
    time.sleep(.1)
