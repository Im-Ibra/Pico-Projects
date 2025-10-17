import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#"Greater than" button connected to the GP0
g_button = digitalio.DigitalInOut(board.GP0)
#Setting it up as Input
g_button.direction = digitalio.Direction.INPUT
#Giving it the Pull up status
g_button.pull = digitalio.Pull.UP

#"Less than" button connected to the GP1
l_button = digitalio.DigitalInOut(board.GP1)
#Setting it up as Input
l_button.direction = digitalio.Direction.INPUT
#Giving it the Pull up status
l_button.pull = digitalio.Pull.UP

keyboard = Keyboard(usb_hid.devices)

while True:
    if l_button.value == False:
        #Less than keycode
        keyboard.press(100)
        keyboard.release_all()
        time.sleep(0.3)
        
    if g_button.value == False:
        #Greater than keycode
        keyboard.press(Keycode.SHIFT)
        keyboard.press(100)
        keyboard.release_all()
        time.sleep(0.3)
