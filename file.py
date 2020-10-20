"""
Helper class for handling storing and updating the file

.txt file contains current light mode, if file has been modified that 
means new data is in the file (updated light mode)
"""


import os
#file class for handling input
class File(object):

    #path to file with data for lights
    filePath = " "

    #time file was last updated
    timeLastUpdated = 0

    #data found in file
    fileData = " "

    def __init__(self, pathTofile):
        self.filePath = pathTofile


    # check if the file has been updated since last checked
    def checkIfUpdated(self):
        try:
            print("here")
            print("file", self.filePath)
            currTime = os.path.getmtime(self.filePath)
            print("currTime", currTime)
            if currTime > self.timeLastUpdated:
                print("updated")
                self.updateData()
                self.timeLastUpdated = currTime
        except Exception as e:
            print("exc", e)

    # if there has been a change to the file, update the variable with the data
    def updateData(self):
        with open(self.filePath) as f:
            self.fileData = f.readline()