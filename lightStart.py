#!/usr/bin/env python3

import time
#from rpi_ws281x import *
import argparse
from flask import Flask, render_template, request

from file import File

import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB

FILE_PATH = "lightSetting.txt"

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbowCycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

# the coloring for these lights is GRB!!
# calls functions depending on light mode selected
def light(currentColor):

    if currentColor == "rainbowCycle":
        print ('rainbowCycle.')
        # Comment this line out if you have RGBW/GRBW NeoPixels
        pixels.fill((255, 0, 0))
        # Uncomment this line if you have RGBW/GRBW NeoPixels
        # pixels.fill((255, 0, 0, 0))
        pixels.show()
        time.sleep(1)
    
        # Comment this line out if you have RGBW/GRBW NeoPixels
        pixels.fill((0, 255, 0))
        # Uncomment this line if you have RGBW/GRBW NeoPixels
        # pixels.fill((0, 255, 0, 0))
        pixels.show()
        time.sleep(1)
    
        # Comment this line out if you have RGBW/GRBW NeoPixels
        pixels.fill((0, 0, 255))
        # Uncomment this line if you have RGBW/GRBW NeoPixels
        # pixels.fill((0, 0, 255, 0))
        pixels.show()
        time.sleep(1)
 
        rainbowCycle(0.001)  # rainbow cycle with 1ms delay per step


if __name__ == "__main__":
    file = File(FILE_PATH)

    try:
        # check if file has a new light mode (update if so)
        while True:
            file.checkIfUpdated()
            print('f.fd', file.fileData)
            if len(file.fileData) == 0:
                print('off')
                light("OFF")
            else:
                print('on')
                light(file.fileData)

    except Exception as e:
        raise e