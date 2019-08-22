import ritaCore.BasicMath as BasicMath
import ritaCore.NaturalLanguage as NaturalLanguage

class ritaCore:
    def __init__(self):
        self.exec_, self.sep = BasicMath.Calculation().usage()

    def readSentence(self, msgs):
        exec_msg = ""
        sep_msg = []
        for msg in msgs:
            if msg in self.sep:
                sep_msg.append(exec_msg)
                sep_msg.append(msg)
                exec_msg = ""
            else:
                exec_msg += msg
        sep_msg.append(exec_msg)
        return sep_msg

    def clearSepMsg(self, sep_msg):
        clearMsg = []
        for msg in sep_msg:
            for text in NaturalLanguage.Separation().getAllAsList():
                clearMsg.append(msg.replace(text, ""))
        return clearMsg

    def cal(self, msgs):
        result = None
        calTask = None
        exec_msg = self.readSentence(msgs)
        exec_msg = self.clearSepMsg(exec_msg)
        for msg in exec_msg:
            if msg in self.sep:
                calTask = self.exec_[msg]
            elif result == None:
                result = NaturalLanguage.Number().dexNum(msg)
            elif calTask != None:
                result = calTask(result, NaturalLanguage.Number().dexNum(msg))
        return result