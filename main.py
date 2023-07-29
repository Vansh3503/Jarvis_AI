from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from loginWindow import LoginWindow  # Import the login window class
import sys
from main_GUI import Ui_main_Gui_file

class MainFile(QWidget):
    def __init__(self):
        super(MainFile, self).__init__()
        print("Main FILE")
        self.mainUI = Ui_main_Gui_file()
        self.mainUI.setupUi(self)
        
        self.mainUI.movie = QtGui.QMovie("Hero_Template.gif")
        self.mainUI.Gif_1.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()
       
        self.mainUI.start_button.clicked.connect(self.open_login_window)
        self.mainUI.start_button_2.clicked.connect(self.close)

    def open_login_window(self):
        self.login_window = LoginWindow()  # Create an instance of the login window
        self.login_window.show()  # Show the login window

# Add the rest of your main_GUI implementation here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainFile()
    ui.show()
    sys.exit(app.exec_())
