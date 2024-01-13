import time
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.i=0 #  FOR DARK MODE

        #  MAIN WINDOW STARTS HERE 

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664,678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QtGui.QIcon("logo1.png"))


        # TEXT BOX STARTS FROM HERE
        
        self.textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(70, 20, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.textbox.setFont(font)
        self.textbox.setObjectName("textbox")
        
        # PUSH BUTTON STARTS FROM HERE
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton#pushButton:hover:!pressed{background-color:green;color:white;}")
        

        # LOADING BAR STARTS FROM HERE

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(215, 160, 281, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        

        # LABEL STARTS FROM HERE

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(20)
        self.label.setGeometry(QtCore.QRect(90, 240, 480, 371))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

                            
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 20))
        self.menubar.setObjectName("menubar")
        
        self.menuHOME = QtWidgets.QMenu(self.menubar)
        self.menuHOME.setObjectName("menuHOME")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionRESET = QtWidgets.QAction(MainWindow,triggered=lambda: self.reset())
        self.actionRESET.setObjectName("actionRESET")
        
        self.menuHOME.addAction(self.actionRESET)
        self.menubar.addAction(self.menuHOME.menuAction())
        
        self.actionDARK = QtWidgets.QAction(MainWindow,triggered=lambda: self.dark(self.i))
        self.actionDARK.setObjectName("actionDARK")
        
        self.menuHOME.addAction(self.actionDARK)
        self.menubar.addAction(self.menuHOME.menuAction())

        self.pushButton.clicked.connect(self.generate)
     

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QRCODE_GEN"))
        self.textbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setStatusTip(_translate("MainWindow", "GENERATE"))
        self.actionRESET.setStatusTip(_translate("MainWindow", "TO RESET THE TEXT"))
        self.pushButton.setText(_translate("MainWindow", "ENTER!"))
        self.label.setText(_translate("MainWindow", "QRCODE"))
        self.menuHOME.setTitle(_translate("MainWindow", "HOME"))
        self.actionRESET.setText(_translate("MainWindow", "RESET"))
        self.actionRESET.setShortcut(_translate("MainWindow", "Ctrl+r"))
        self.actionDARK.setText(_translate("MainWindow", "DARK MODE"))
        self.actionDARK.setStatusTip(_translate("MainWindow","TO SWITCH MODES"))
        self.actionDARK.setShortcut(_translate("MainWindow", "Ctrl+b"))
    def generate(self):
        for i in range(0,101,5):
            time.sleep(.02)
            self.progressBar.setValue(i)
        self.y=self.textbox.toPlainText()
        self.z=qrcode.make(self.y)
        hrf="qr.png"
        self.z.save(hrf)
        pixmap =QPixmap(hrf)
        self.label.setPixmap(pixmap)
    def reset(self):
        self.textbox.setText("")
        self.label.setText("QRCODE")
        self.progressBar.setValue(0)
        
    def dark(self,i):
        if i%2==0:    
            #designing menu bar

            # self.pushButton.setStyleSheet("Q#pushButton:hover:!pressed{background-color:green;}")
            self.menubar.setStyleSheet("background-color:#474746;color:#FCD704;")
            self.menuHOME.setStyleSheet("background-color:red;color:white")
            self.statusbar.setStyleSheet("background-color:#474746;color:white;")
            self.textbox.setStyleSheet("background-color:black;color:white;")
            self.centralwidget.setStyleSheet("background-color:#2e2c2c;color:white;")
            self.pushButton.setStyleSheet("background-color:black;color:white;")
            self.pushButton.setStyleSheet("QPushButton#pushButton:hover:!pressed{background-color:green;color:white;}")
            self.actionDARK.setText("BRIGHT")

        else:
            #designing menu bar
            # self.pushButton.setStyleSheet("Q#pushButton:hover:!pressed{background-color:green;}")

            self.menubar.setStyleSheet("background-color:#FCF8E5;color:black;")
            self.menuHOME.setStyleSheet("background-color:red;")
            self.pushButton.setStyleSheet("QPushButton#pushButton:hover:!pressed{background-color:green;color:black;}")
            self.statusbar.setStyleSheet("background-color:white;color:black;")
            self.textbox.setStyleSheet("background-color:white;color:black;")
            self.centralwidget.setStyleSheet("background-color:#E7E5DE;color:black;")
            self.pushButton.setStyleSheet("background-color:white;color:black;")
            self.actionDARK.setText("DARK")
        self.i=i+1
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
