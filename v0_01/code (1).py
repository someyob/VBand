# VBand Interface
# v0.1, non-interrupt version
# https://hamradio.solutions/vband/

import time

import board
import digitalio
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

pixel.brightness = 0.3
pixel.fill((0, 0, 0))  #just turn off the neopixel

right_pin = digitalio.DigitalInOut(board.A0)
right_pin.direction = digitalio.Direction.INPUT
right_pin.pull = digitalio.Pull.UP

left_pin = digitalio.DigitalInOut(board.A1)
left_pin.direction = digitalio.Direction.INPUT
left_pin.pull = digitalio.Pull.UP

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# print("Waiting for key pin...")
while True:

    if not left_pin.value:  # pulled low?
        keyboard.press(Keycode.LEFT_BRACKET)
        led.value = True
        while not left_pin.value:
            time.sleep(0.001)
        keyboard.release(Keycode.LEFT_BRACKET)
        led.value = False
    if not right_pin.value:  
        keyboard.press(Keycode.RIGHT_BRACKET)    
        led.value = True                         
        while not right_pin.value:               
            time.sleep(0.001)
        keyboard.release(Keycode.RIGHT_BRACKET)
        led.value = False
    time.sleep(0.001)
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
