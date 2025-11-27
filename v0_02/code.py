# VBand Interface
# v0.2, corrected code for simultaneous paddle press
# https://hamradio.solutions/vband/
# VBand will apply the right iambic logic

import time

import board
import digitalio
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

right_pin = digitalio.DigitalInOut(board.A0)
right_pin.direction = digitalio.Direction.INPUT
right_pin.pull = digitalio.Pull.UP

left_pin = digitalio.DigitalInOut(board.A1)
left_pin.direction = digitalio.Direction.INPUT
left_pin.pull = digitalio.Pull.UP

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.3
pixel.fill((0, 0, 0))  #just turn off the neopixel

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# print("Waiting for key pin...")
while True:
    left_key = not left_pin.value   # pulled low ?
    right_key = not right_pin.value
    if left_key:
        keyboard.press(Keycode.LEFT_BRACKET)
    else:
        keyboard.release(Keycode.LEFT_BRACKET)
    if right_key:
        keyboard.press(Keycode.RIGHT_BRACKET)
    else:
        keyboard.release(Keycode.RIGHT_BRACKET)
    if left_key or right_key:
        led.value = True
    else:
        led.value = False
    #time.sleep(0.001)
 
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    