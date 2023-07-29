from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5 import QtGui
from loginJarvis import Ui_Form
from face_recognition1 import mainFile
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.loginUI = Ui_Form()
        self.loginUI.setupUi(self)

        # Create a QMovie object with the path to your animated GIF
        self.movie = QtGui.QMovie("C:\\Users\\hp\\PycharmProjects\\Jarvis_Ultra\\Interface\\giphy.gif")
        self.loginUI.wrong.setMovie(self.movie)

        # Hide the animation by default
        self.loginUI.wrong.hide()

        self.loginUI.login_button.clicked.connect(self.ValidateLogin)
        self.loginUI.password.setEchoMode(QLineEdit.Password)
        self.loginUI.exit_but.clicked.connect(self.close)
        self.loginUI.retry_butt.clicked.connect(self.retrybutton)
        
    
    # Add the rest of your loginJarvis implementation here

    def ValidateLogin(self):
        username = self.loginUI.usrname.text()
        pas = self.loginUI.password.text()

        if username == 'vansh' and pas == 'vansh2003':
            print("Login Successful")
            self.login_window = mainFile() # Create an instance of the login window
            self.login_window.show()  # Show the login window


        else:
            self.startMovie()

    def retrybutton(self):
        self.loginUI.usrname.clear()
        self.loginUI.password.clear()  # Corrected: added parentheses to clear() method
        self.stopMovie()
    def facereg(self):
        self.lo= LoginWindow()  # Create an instance of the login window
        self.login_window.show()
    def startMovie(self):
        self.loginUI.wrong.show()
        self.movie.start()

    def stopMovie(self):
        self.movie.stop()
        self.loginUI.wrong.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LoginWindow()
    ui.show()
    sys.exit(app.exec_())