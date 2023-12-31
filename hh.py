# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisMainGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 750)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Jarvis_label = QtWidgets.QLabel(Form)
        self.Jarvis_label.setGeometry(QtCore.QRect(430, 10, 431, 111))
        self.Jarvis_label.setText("")
        self.Jarvis_label.setPixmap(QtGui.QPixmap("avengero-regular (2).png"))
        self.Jarvis_label.setScaledContents(True)
        self.Jarvis_label.setObjectName("Jarvis_label")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(430, 140, 431, 281))
        self.label.setStyleSheet("border:1px dashed white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Jarvis_Gui (1).gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(870, 140, 401, 281))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Iron_Template_2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 430, 1301, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1191, 231))
        font = QtGui.QFont()
        font.setFamily("The Mighty Avengers")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.entecomm = QtWidgets.QLineEdit(self.frame)
        self.entecomm.setGeometry(QtCore.QRect(0, 230, 1191, 41))
        font = QtGui.QFont()
        font.setFamily("The Mighty Avengers")
        font.setPointSize(15)
        self.entecomm.setFont(font)
        self.entecomm.setObjectName("entecomm")
        self.start_button_3 = QtWidgets.QPushButton(self.frame)
        self.start_button_3.setGeometry(QtCore.QRect(1110, 240, 71, 21))
        self.start_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button_3.setStyleSheet("border-image: url(avengero-regular (3).png);\n"
"background-color:transparent;")
        self.start_button_3.setText("")
        self.start_button_3.setObjectName("start_button_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 270, 1281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("wave.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.start_button_2 = QtWidgets.QPushButton(Form)
        self.start_button_2.setGeometry(QtCore.QRect(1200, 700, 81, 31))
        self.start_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button_2.setStyleSheet("border-image: url(avengero-regular.png);\n"
"background-color:transparent;")
        self.start_button_2.setText("")
        self.start_button_2.setObjectName("start_button_2")
        self.DOUBLE = QtWidgets.QLabel(Form)
        self.DOUBLE.setGeometry(QtCore.QRect(10, -10, 411, 431))
        self.DOUBLE.setStyleSheet("border:1px solid white;")
        self.DOUBLE.setText("")
        self.DOUBLE.setPixmap(QtGui.QPixmap("gyhf.jpg"))
        self.DOUBLE.setScaledContents(True)
        self.DOUBLE.setObjectName("DOUBLE")
        self.P1 = QtWidgets.QLabel(Form)
        self.P1.setGeometry(QtCore.QRect(60, 30, 311, 131))
        self.P1.setText("")
        self.P1.setPixmap(QtGui.QPixmap("B.G_Template_1.gif"))
        self.P1.setScaledContents(True)
        self.P1.setObjectName("P1")
        self.P2 = QtWidgets.QLabel(Form)
        self.P2.setGeometry(QtCore.QRect(40, 190, 351, 211))
        self.P2.setStyleSheet("border:1px solid white;")
        self.P2.setText("")
        self.P2.setPixmap(QtGui.QPixmap("__1.gif"))
        self.P2.setScaledContents(True)
        self.P2.setObjectName("P2")
        self.P3 = QtWidgets.QLabel(Form)
        self.P3.setGeometry(QtCore.QRect(876, 1, 401, 131))
        self.P3.setStyleSheet("border:1px solid white;")
        self.P3.setText("")
        self.P3.setPixmap(QtGui.QPixmap("loading_1.gif"))
        self.P3.setScaledContents(True)
        self.P3.setObjectName("P3")
        self.speak = QtWidgets.QLabel(Form)
        self.speak.setGeometry(QtCore.QRect(90, 200, 261, 181))
        self.speak.setStyleSheet("\n"
"border-image: url(d921358f2b283ff6d4e364dde38ee40a.gif);")
        self.speak.setText("")
        self.speak.setScaledContents(True)
        self.speak.setObjectName("speak")
        self.sleeping = QtWidgets.QLabel(Form)
        self.sleeping.setGeometry(QtCore.QRect(86, 211, 271, 171))
        self.sleeping.setStyleSheet("Ntuks.gif);")
        self.sleeping.setText("")
        self.sleeping.setObjectName("sleeping")
        self.frame.raise_()
        self.Jarvis_label.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.start_button_2.raise_()
        self.DOUBLE.raise_()
        self.P1.raise_()
        self.P2.raise_()
        self.P3.raise_()
        self.speak.raise_()
        self.sleeping.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setPlaceholderText(_translate("Form", "Terminal Output Goes Here"))
        self.entecomm.setPlaceholderText(_translate("Form", "Enter Your Command"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
