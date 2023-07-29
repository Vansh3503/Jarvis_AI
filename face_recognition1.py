import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from face_rec import Ui_Form
import cv2
import face_recognition
import numpy as np
def namelist(nameofimg):
    if nameofimg.startswith('rj',0):
        return "RDJ"
    if nameofimg.startswith('rj',0):
        return "RDJ"
    if nameofimg.startswith('v',0):
        return "vansh"
    if nameofimg.startswith('v',0):
        return "vansh"
    if nameofimg.startswith('cap',0):
        return "steve"
    

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()

        self.faceUI = Ui_Form()
        self.faceUI.setupUi(self)
        self.faceUI.exit_but.clicked.connect(self.close)

        
        self.faceUI.login_button.clicked.connect(self.runProgram)
        self.name = "Unknown"

    def runProgram(self):
        cameraName = 0
        self.encodeImages(cameraName)

    def encodeImages(self, cameraName):
        print("Encoding Started")

        self.capture = cv2.VideoCapture(cameraName)
        
        
        self.timer = QTimer(self)
        path = 'images'

        if not os.path.exists(path):
            os.mkdir(path)

        images = []
        self.classNames = []
        self.encodeList = []

        photoList = os.listdir(path)

        for cl in photoList:
            currentImage = cv2.imread(f'{path}/{cl}')
            images.append(currentImage)
            self.classNames.append(os.path.splitext(cl)[0])

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            box = face_recognition.face_locations(img)
            encodeCurFrame = face_recognition.face_encodings(img, box)[0]

            self.encodeList.append(encodeCurFrame)

        print("Images encoded Succesfully")

        self.timer.timeout.connect(self.updateFrames)
        self.timer.start(10)

    def updateFrames(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image, self.encodeList, self.classNames, 1)

    def displayImage(self, image, encodeList, classNames, window=1):
        image = cv2.resize(image, (451, 301))
        try:
            self.faceReco(image, encodeList, classNames)

        except Exception as e:
            print(e)

        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA888

            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.faceUI.camera.setPixmap(QPixmap.fromImage(outImage))
            self.faceUI.camera.setScaledContents(True)
            if self.name == "vansh":
                self.connecttomainfile()
                self.timer.stop()



    def faceReco(self, image, encodeList, classNames):
        faceofcurrframe = face_recognition.face_locations(image)
        encodecurrframe = face_recognition.face_encodings(image, faceofcurrframe)

        for encodeFace, faceLocation in zip(encodecurrframe, faceofcurrframe):
            match = face_recognition.compare_faces(encodeList, encodeFace, tolerance=0.5)
            facedist = face_recognition.face_distance(encodeList, encodeFace)
            self.name = "Unknown"
            besrMatchIndex = np.argmin(facedist)

            if match[besrMatchIndex]:
                self.name = classNames[besrMatchIndex]
                self.name=namelist(self.name)
                y1, x2, y2, x1 = faceLocation
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, self.name, (x1 - 6, y2 + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        return image
    

    
    def connecttomainfile(self):
        from subprocess import call
        self.close()

        call(["python","finalinterface.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())
