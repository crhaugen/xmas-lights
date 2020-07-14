#!/usr/bin/env python3
 
import time
from neopixel import *
import argparse
from flask import Flask, render_template, request
from thread import start_new_thread
from file import File


currentColor = "White"
newColor = "White"
FILE_PATH = "lightSetting.txt"


# LED strip configuration:
# Based on my led light strip (might have to change for different light strips)
LED_COUNT = 300     # Number of LED pixels.
LED_PIN  = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
 
 
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
 
def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
 
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)
 
def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
 
def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
 
def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# the coloring for these lights is GRB!!
def light(currentColor):
    global strip
    strip.begin()
    colorWipe(strip, Color(0,0,0), 10)

    print('LIGHT!!!', currentColor)
   
    if currentColor == "colorWipeSeahawks":
        print ('colorWipeSeahawks.')
        colorWipe(strip, Color(34, 0, 68))  # collage navy
        colorWipe(strip, Color(190, 105, 40))  # action green
        colorWipe(strip, Color(172, 165, 175))  # wolf grey
 
    elif currentColor == "colorWipe":
        print ('colorWipe.')
        colorWipe(strip, Color(255, 0, 0))  # Green wipe
        colorWipe(strip, Color(0, 255, 0))  # Red wipe
        colorWipe(strip, Color(0, 0, 255))  # Blue wipe


    elif currentColor == "theaterChase":
        print ('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase

    elif currentColor == "rainbow":
        print ('Rainbow stuff.')
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)

    elif currentColor == "rainbowCycle":
        print ('rainbow cycle')
        rainbowCycle(strip)

    elif currentColor == "OFF":
        colorWipe(strip, Color(0,0,0), 10)


   
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
