#!/usr/bin/env python3

import time
import argparse
from flask import Flask, render_template, request
import board
import neopixel

from file import File


pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.RGB # coloring for my lights are RGB

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

def colorWipe(color):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(50/1000.0)

# the coloring for these lights is RGB
# calls functions depending on light mode selected
def light(currentColor):

    if currentColor == "rainbowCycle":
        print ('rainbowCycle.')
        rainbowCycle(0.001)

    elif currentColor == "halloweenWipe":
        print('halloween')
        orange = (255, 165, 0)
        purple = (128, 0, 128)
        limegreen = (50, 205, 50)

        colorWipe(orange)
        colorWipe(purple)
        colorWipe(limegreen)

    elif currentColor == 'OFF':
        print('off')
        pixels.fill((0, 0, 0))
        pixels.show()

    time.sleep(1)


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