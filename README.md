# xmas-lights

Internet controlled lights! 

Using a Raspberry Pi and Python to control a LED NeoPixel strip.  

## How it works

There are 2 main programs that allow the lights to be run and controlled remotely.

The first program creates a server using Flask that displays a simple static website with buttons that change the lights. As of now the server is just a developer server (locally hosted) 

**Webpage with buttons to controll the lights**
![Alt Text](https://github.com/crhaugen/xmas-lights/blob/Pictures/xmaslights.JPG)

The second program is controlling the light settings (using neo-pixel library [Link](https://github.com/adafruit/Adafruit_NeoPixel)) and checking if a new request came from the webpage.

Both programs are being run on a Raspberry Pi.


**Raspberry Pi Setup**
![Alt Text](https://github.com/crhaugen/xmas-lights/blob/Pictures/0714201128.jpg)


**Lights in Action**
![Alt Text](https://github.com/crhaugen/xmas-lights/blob/Pictures/0714201125a.jpg)



## Future Improvments
* add more lights (need to add more power)
* Discord controlled (by bot?) 



### Software + Equipment
* Python
* Flask
* LED light strip
* Raspberry Pi
