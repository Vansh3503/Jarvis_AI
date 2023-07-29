# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facerec.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Jarvis_label = QtWidgets.QLabel(Form)
        self.Jarvis_label.setGeometry(QtCore.QRect(390, 10, 271, 61))
        self.Jarvis_label.setText("")
        self.Jarvis_label.setPixmap(QtGui.QPixmap("avengero-regular (2).png"))
        self.Jarvis_label.setScaledContents(True)
        self.Jarvis_label.setObjectName("Jarvis_label")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(620, 200, 37, 12))
        self.label.setText("")
        self.label.setObjectName("label")
        self.iron = QtWidgets.QLabel(Form)
        self.iron.setGeometry(QtCore.QRect(500, 90, 571, 301))
        self.iron.setText("")
        self.iron.setPixmap(QtGui.QPixmap("Iron_Template_2.jpg"))
        self.iron.setScaledContents(True)
        self.iron.setObjectName("iron")
        self.camera = QtWidgets.QLabel(Form)
        self.camera.setGeometry(QtCore.QRect(20, 90, 451, 301))
        self.camera.setStyleSheet("border:2px solid white;\n"
"background-color: rgb(0, 0, 0);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.exit_but = QtWidgets.QPushButton(Form)
        self.exit_but.setGeometry(QtCore.QRect(240, 650, 161, 61))
        self.exit_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_but.setStyleSheet("border-image: url(avengero-regular.png);\n"
"background-color:transparent;")
        self.exit_but.setText("")
        self.exit_but.setObjectName("exit_but")
        self.login_button = QtWidgets.QPushButton(Form)
        self.login_button.setGeometry(QtCore.QRect(30, 650, 161, 61))
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("border-image: url(hello.png);\n"
"border-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color:transparent;")
        self.login_button.setText("")
        self.login_button.setObjectName("login_button")
        self.loading = QtWidgets.QLabel(Form)
        self.loading.setGeometry(QtCore.QRect(300, 400, 691, 231))
        self.loading.setStyleSheet("background-color:transparent;")
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("initial.gif"))
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())