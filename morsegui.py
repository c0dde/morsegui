from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import RPi.GPIO as GPIO
import time

## hardware
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

## Morse code dictionary
DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'} 


## Ui class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(217, 110)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 151, 16))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 151, 21))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        app.aboutToQuit.connect(self.closeEvent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Morse code convertor"))
        self.pushButton.setText(_translate("MainWindow", "Convert to Morse code"))
        # Give something the button to do
        self.pushButton.clicked.connect(self.decode)

    ## Convert name to led flash
    def decode (self):
        Total = ''
        NAME = self.textEdit.toPlainText()
        if len(NAME) <= 12:
            NAME = NAME.upper()
            for char in NAME:
                Total = Total + DICT[char]
            for morse in Total:
                if morse == '-':
                    GPIO.output(14,GPIO.HIGH)
                    time.sleep(0.7)
                    GPIO.output(14,GPIO.LOW)
                    time.sleep(0.2)
                else:
                    GPIO.output(14,GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(14,GPIO.LOW)
                    time.sleep(0.2)
        else:
        ## Alert
            QMessageBox.information(MainWindow, 'Error', 'Maxinum charater is 12.')
            


    
    def closeEvent(self):
        GPIO.cleanup()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    


