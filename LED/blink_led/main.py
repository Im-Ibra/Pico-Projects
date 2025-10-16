from machine import Pin
import time

#Pico's integrated LED
pico_led = Pin("LED", Pin.OUT)

#Led connected to GPIO 0
led = Pin(0, Pin.OUT)

while True:
    pico_led.toggle()
    led.toggle()
    time.sleep(.5)