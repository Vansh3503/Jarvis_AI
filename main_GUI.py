# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_Gui_file(object):
    def setupUi(self, main_Gui_file):
        main_Gui_file.setObjectName("main_Gui_file")
        main_Gui_file.resize(800, 600)
        main_Gui_file.setStyleSheet("\n"
                                    "background-color: rgb(0, 0, 0);")
        self.Jarvis_label = QtWidgets.QLabel(main_Gui_file)
        self.Jarvis_label.setGeometry(QtCore.QRect(250, 10, 301, 81))
        self.Jarvis_label.setText("")
        self.Jarvis_label.setPixmap(QtGui.QPixmap("avengero-regular (2).png"))
        self.Jarvis_label.setScaledContents(True)
        self.Jarvis_label.setObjectName("Jarvis_label")
        self.Gif_1 = QtWidgets.QLabel(main_Gui_file)
        self.Gif_1.setGeometry(QtCore.QRect(6, 101, 791, 421))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("Hero_Template.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")
        self.start_button = QtWidgets.QPushButton(main_Gui_file)
        self.start_button.setGeometry(QtCore.QRect(10, 530, 161, 61))
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setStyleSheet("border-image: url(avengero-regular (1).png);\n"
                                        "background-color:transparent;")
        self.start_button.setText("")
        self.start_button.setObjectName("start_button")
        self.start_button_2 = QtWidgets.QPushButton(main_Gui_file)
        self.start_button_2.setGeometry(QtCore.QRect(630, 530, 161, 61))
        self.start_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button_2.setStyleSheet("border-image: url(avengero-regular.png);\n"
                                          "background-color:transparent;")
        self.start_button_2.setText("")
        self.start_button_2.setObjectName("start_button_2")
        self.start_button_3 = QtWidgets.QPushButton(main_Gui_file)
        self.start_button_3.setGeometry(QtCore.QRect(210, 530, 161, 61))
        self.start_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button_3.setStyleSheet("border-image: url(avengero-regular 9.png);\n"
                                          "background-color:transparent;")
        self.start_button_3.setText("")
        self.start_button_3.setObjectName("start_button_3")

        self.retranslateUi(main_Gui_file)
        QtCore.QMetaObject.connectSlotsByName(main_Gui_file)

    def retranslateUi(self, main_Gui_file):
        _translate = QtCore.QCoreApplication.translate
        main_Gui_file.setWindowTitle(_translate("main_Gui_file", "main_Gui_file"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_Gui_file = QtWidgets.QWidget()
    ui = Ui_main_Gui_file()
    ui.setupUi(main_Gui_file)
    main_Gui_file.show()
    sys.exit(app.exec_())
