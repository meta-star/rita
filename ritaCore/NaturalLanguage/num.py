class Number:
    def __init__(self):
        self.numDict = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }

    def dexNum(self, text):
        result = 0
        for x,y in enumerate(text):
            result += (10**(len(text)-(x+1)))*self.numDict[y]
        return result

    def getAll(self):
        return  self.numDict


    def getAllAsList(self):
        sepList = []
        for sep in self.numDict:
            sepList.append(self.numDict[sep])
        return sepList

    def get(self, name):
        return self.numDict[name]