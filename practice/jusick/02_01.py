import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first pyqt5")
        self.setGeometry(100,100,500,500)
        self.setWindowIcon(QIcon("./magic.png"))

        btn = QPushButton(text="hello", parent=self)
        btn.move(10,10)
        btn.clicked.connect(self.hello)

        exit_btn = QPushButton(text="Exit", parent=self)
        exit_btn.move(50,50)
        exit_btn.clicked.connect(self.quit)

    def quit(self):
        QApplication.instance().quit()

    
    def hello(self):
        print("Hello button clicked!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec_()     # event loop
