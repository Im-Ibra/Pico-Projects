from machine import Pin
import time

#Led connected to GPIO 0
led = Pin(0, Pin.OUT)

#Push button connected to GPIO 1 a set the Input status as pull up
button = Pin(1, Pin.IN, Pin.PULL_UP)
 
while True:
    if button.value() == 0:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
