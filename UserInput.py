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
        #so now I need to isolate the condition when the "=" button on the GUI
        #is pressed. 
            
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
            #set tempValue2, clear the output, display the calculated result.
            self.tempValue2 = int(self.outPut.text())
            self.outPut.clear()
            #perform the math operation.
            #below is a temporary example of output...
            #conditions for the operands... *4.
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
    """def _userInput(self, buttonName):
        print(buttonName, " has been pressed.")
        for op in self.operands:
            if buttonName == op:
                self.opFlag = True
                self.operand = op
                
                self.tempValue1 = int(self.outPut.text())
                self.outPut.clear()
                print(self.tempValue1)
                print(op)
                self.outPut.setText(op)
                #i think i need to store and clear the output text here.
                #run throught it again and understand it. 
        if not self.opFlag:
            #do this... probably a good idea.
            print("stuff")
            #will need to return the number to an object in the main program
            self.outPut.setText(self.outPut.text() + buttonName)
            
        if self.opFlag:
            #if the above two conditions are met, clear the output, which will
            #be an operand! I only want to clear this once.
            #i can easily put in a condition here to isolate the scenario, so
            #to speak, I'm just thinking of a better/beuatiful way of writing
            #it. 
            self.outPut.clear()
            #now output the new userinput, which will be an integer entry..
            self.outPut.setText(self.outPut.text() + buttonName)
            #clear the flag so we can jump back into the earlier condition(opFlag == False)
            self.ofFlag = False
        if buttonName == "=" and self.tempValue1 > 0:
                #do calculation.
                if self.operand == "*":
                    print(self.tempValue1 * int(self.outPut.text()))
        elif self.tempValue1 == 0:
            print("require first input before using the ""equals"" symbol.")
    """
