import time
import argparse
from flask import Flask, render_template, request

app = Flask(__name__)

# .txt file contain the mode lights are currently set to 
FILE_PATH = "lightSetting.txt"

def updateFile(data):

    with open(FILE_PATH, 'w') as f:
        f.write(data)
        f.close()


#sets up webpage and handle request from the site
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
    app.run(host='0.0.0.0', port=5055, threaded=True)
