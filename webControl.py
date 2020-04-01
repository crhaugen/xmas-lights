import time
from neopixel import *
import argparse
from flask import Flask, render_template, request
from thread import start_new_thread
import json

app = Flask(__name__)
FILE_PATH = 'lightSetting.txt'

def updateFile(data):

    with open(FILE_PATH, 'w') as f:
        f.write(data)
        f.close()




#runs when button is pressed or not
@app.route('/', methods=['GET', 'POST'])
def Main():
    global currentColor
    print(request.get_data(as_text=True))
    if request.method == 'POST':
        while 'colorWipe' in request.form:
            print('colorWipe', currentColor)
            currentColor = 'colorWipe'
            light()
        while 'theaterChase' in request.form:
            currentColor = 'theaterChase'
            light()
            print('theaterChase', currentColor)
       
    elif request.method == 'GET':
        return render_template('homePage.html')

   
    return render_template('homePage.html')
   
if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
