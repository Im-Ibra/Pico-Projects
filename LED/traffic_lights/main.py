from machine import Pin
import time

#Red led connected to GPIO 5
r_led = Pin(5, Pin.OUT)

#Yellow led connected to GPIO 9
y_led = Pin(9, Pin.OUT)

#Green led connected to GPIO 13
g_led = Pin(13, Pin.OUT)

#List with all leds
traffic_light =  [g_led, y_led, r_led]

while True:
    #Loops through all the leds inside the traffic_light list
    for leds in traffic_light:
        leds.value(1)
        time.sleep(1)
        leds.value(0)