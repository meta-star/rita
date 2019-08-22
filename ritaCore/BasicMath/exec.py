class Calculation:
    def __init__(self):
        self.exec_code = ["+", "-", "*", "/"]

    def add(self, num, add):
        return num + add

    def sub(self, num, sub):
        return num - sub

    def mul(self, num, mul):
        return num * mul

    def div(self, num, div):
        return num / div

    def usage(self):
        self.exec = {
            self.exec_code[0]: self.add,
            self.exec_code[1]: self.sub,
            self.exec_code[2]: self.mul,
            self.exec_code[3]: self.div
        }
        return self.exec, self.exec_code