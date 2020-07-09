import os
print os.environ['PATH']
#file class for handling input
class File(object):

    #path to file with data for lights
    filePath = " "

    #to see if file has new data
    timeLastUpdated = 0

    #data found in file
    fileData = " "

    def __init__(self, pathTofile):
        self.filePath = pathTofile
        print("path", pathTofile)

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

    def updateData(self):

        with open(self.filePath) as f:
            self.fileData = f.readline()
	    print('data', self.fileData)



