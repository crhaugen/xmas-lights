import os

class File(object):

    #path to file with data for lights
    filePath = " "

    #to see if file has new data
    timeLastUpdated = 0

    #data found in file
    fileData = " "

    def __init__(self, pathTofile):
        self.filePath = pathTofile

    def checkIfUpdated(self):
        try:
            currTime = os.path.getmtime(self.filePath)

            if currTime > self.timeLastUpdated:
                self.updateData()
                self.timeLastUpdated = currTime
        except:
            pass

    def updateData(self):

        with open(self.filePath) as f:
            self.fileData = f.readline()



