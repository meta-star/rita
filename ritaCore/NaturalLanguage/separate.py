class Separation:
    def __init__(self):
        self.allSepDict = {}
        self.allSepDict["space"] = " "

    def getAll(self):
        return  self.allSepDict


    def getAllAsList(self):
        sepList = []
        for sep in self.allSepDict:
            sepList.append(self.allSepDict[sep])
        return sepList

    def get(self, name):
        return self.allSepDict[name]