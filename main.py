수정수정수정

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    sys.exit(app.exec_())
    
    #myWindow.show()
    #app.exec_()