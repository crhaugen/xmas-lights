# xmas-lights

Web controlled lights! 

Using a Raspberry Pi and Python to control a LED NeoPixel strip.  

## How it works

There are 2 main programs that allow the lights to be run and controlled remotely.

The first program creates a server using Flask that displays a simple static website with buttons that change the lights. As of now the server is just a developer server (locally hosted) 

The second program is controlling the light settings (using neo-pixel library [Link](https://github.com/adafruit/Adafruit_NeoPixel)) and checking if a new reqeust came from the webpage.

Both programs are being run on a Raspberry Pi.



## Future Improvments
* add more lights (need to add more power)
* Discord controlled (by bot?) 



### Software + Equipment
* Python
* Flask
* LED light strip
* Raspberry Pi
