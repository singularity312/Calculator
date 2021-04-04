import sys
from UserInput import UserInput
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit
    )
from PySide6 import QtCore
from PySide6.QtGui import QFont
from functools import partial

calculatorId = ["%",
                "CE",
                "C",
                "BACK",
                "1/X",
                "X^2",
                "2SqrtX",
                "/",
                "7",
                "8",
                "9",
                "*",
                "4",
                "5",
                "6",
                "-",
                "1",
                "2",
                "3",
                "+",
                "+/-",
                "0",
                ".",
                "="]

memoryRibbonId = ["MC",
                  "MR",
                  "M+",
                  "M-",
                  "MS",
                  "Mv"]

class Button(QPushButton):

    def __init__(self, buttonId):
        super().__init__(buttonId)
        self.name = buttonId

class BaseLayout(QVBoxLayout):
    def __init__(self, parent = None):
        super().__init__(parent)
        
class Grid(QGridLayout):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.buttons = []
        self.buttonStrings = []
        self.notDone = True
        self.index = 0
             
    def _addButtonTest(self):
        self.atRow = 0
        self.atColumn = 0
        for buttons in self.buttons:
            buttons.setFixedSize(75, 50)
        while self.notDone:
            super().addWidget(self.buttons[self.index],
                              self.atRow, self.atColumn, 1, 1)
            self.index += 1
            self.atColumn += 1
            if self.atColumn == 4:
               print(self.atRow)
               self.atRow += 1
               self.atColumn = 0
            if self.index == len(self.buttons):
                self.notDone = False
        self.index = 0
        self.notDone = True  
            
    def _addNumberDisplayField(self):
        self.displayField = QLineEdit()
        super().addWidget(self.displayField, 0, 0, -1, 1)

    def _createButtons(self):
        for calcId in calculatorId:
            self.buttonStrings.append(calcId)
            print(calcId)
            self.button = Button(self.buttonStrings[self.index])
            self.buttons.append(self.button)
            self.index += 1
        self.index = 0

calcApp = QApplication([])
windowSize = QtCore.QSize(340, 500)
window = QWidget()
window.setWindowTitle("Calculator")
window.setFixedSize(windowSize)
baseLayout = BaseLayout(window)

#create the Line/Text display widget ***
outPutField = QLineEdit("")
outPutField.setMaximumWidth(400)
#need a font...***

outPutField.setAlignment(QtCore.Qt.AlignRight)
outPutField.setMinimumHeight(75)
outPutField.setReadOnly(True)
outPutFieldFont = QFont("OPField Font", 50)
outPutField.setFont(outPutFieldFont)

baseLayout.addWidget(outPutField)

#need to create the memory ribbon field, so a horizontal box layout.*** 
memoryRibbonLayout = QHBoxLayout()
baseLayout.addLayout(memoryRibbonLayout)

#need to add several memory ribbon buttons.***
buttons = []
for i in range(0, 6):
    button = Button(memoryRibbonId[i])
    button.setFixedSize(48, 30)    
    buttons.append(button)

for button in buttons:
    memoryRibbonLayout.addWidget(button)

gridLayout = Grid()
gridLayout.setColumnMinimumWidth(0, 1)
                          
baseLayout.addLayout(gridLayout)
gridLayout._createButtons()
gridLayout._addButtonTest()

uInput = UserInput(outPutField)                        

for button in gridLayout.buttons:
    button.clicked[bool].connect(lambda clicked, x=button: uInput._userInput(x.name))

window.show()
sys.exit(calcApp.exec_())


