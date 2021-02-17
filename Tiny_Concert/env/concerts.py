# class definition written by Dr. Ben Geisler
class Concerts():  
    foo = 'bar' #member variable on Concerts class  
    def __init__(self):  #this is construtor
        self.concertsDict = {
            "None": "None"        
        }
        with open("data/concerts/concerts.txt") as f:        
            while line := f.readline():
                self.concertsDict.update(self.process(line))
    def process(self, line): #member function
        concertsDict = {
            "None": "None"        
        }
        linedata = line.split(",")
        #print(linedata)
        #print(linedata[0])
        #print(linedata[1])
        concertsDict[linedata[0]] = linedata[1]        
        return concertsDict

    