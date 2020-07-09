import time
import argparse
from flask import Flask, render_template, request

app = Flask(__name__)
FILE_PATH = 'lightSetting.txt'

def updateFile(data):

    with open(FILE_PATH, 'w') as f:
        f.write(data)
        f.close()




#runs when button is pressed or not
@app.route('/', methods=['GET', 'POST'])
def Main():
    
    if request.method == 'POST':

        data = ''
        for val in request.form:
            data = val

        updateFile(data)
        
       
    elif request.method == 'GET':
        return render_template('homePage.html')

   
    return render_template('homePage.html')
   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, threaded=True)
