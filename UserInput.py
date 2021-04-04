class UserInput:
    def __init__(self, outputField):
        self.tempValue1 = 0
        self.tempValue2 = 0
        self.operand = ""
        self.opFlag = False
        self.operands = ["*", "+", "/", "-"]
        self.outPut = outputField

    def _userInput(self, buttonName):
        print(buttonName, " has been pressed.")
            
        for op in self.operands:
            if buttonName == op:
                self.opFlag = True
                self.operand = op
            
        if (self.opFlag == False and self.tempValue1 == 0 or
                self.opFlag == True and self.tempValue1 > 0 and buttonName != "="
            and buttonName != "CE"):
            self.outPut.setText(self.outPut.text() + buttonName)
    
        elif self.opFlag == True and self.tempValue1 == 0:
            self.tempValue1 = int(self.outPut.text())
            self.outPut.clear()
            self.outPut.setText(self.operand)
            self.opFlag = False

        elif self.tempValue1 > 0 and self.opFlag == False:
            print(self.tempValue1)
            self.outPut.clear()
            self.outPut.setText(buttonName)
            print(buttonName, " has been pressed.")
            self.opFlag = True
            
        elif self.opFlag == True and self.tempValue1 > 0 and buttonName == "=":
            self.tempValue2 = int(self.outPut.text())
            self.outPut.clear()
            
            if self.operand == "+":
                self.outPut.setText(str(self.tempValue1 + self.tempValue2))
                print(self.tempValue1 + self.tempValue2)
            elif self.operand == "-":
                self.outPut.setText(str(self.tempValue1 - self.tempValue2))
                print(self.tempValue1 - self.tempValue2)
            elif self.operand == "*":
                self.outPut.setText(str(self.tempValue1 * self.tempValue2))
                print(self.tempValue1 * self.tempValue2)
            elif self.operand == "/":
                self.outPut.setText(str(self.tempValue1 / self.tempValue2))
                print(self.tempValue1 / self.tempValue2)
                
        elif buttonName == "CE":
            self.outPut.setText("")
            self.tempValue1 = 0
            self.tempValue2 = 0
            self.operand = ""
            self.opFlag = False
