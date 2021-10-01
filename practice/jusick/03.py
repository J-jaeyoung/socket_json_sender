import sys
from PyQt5.QtWidgets import *

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = True
        self.setGeometry(100,100,600,600)
        self.btn = QPushButton("exit", self)
        self.btn.move(10,10)
        self.btn.clicked.connect(self.button_handler)
        self.btn.resize(100,100)
        self.btn.setEnabled(True)

        self.label = QLabel("Hello", self)
        self.label.move(200,200)

    def button_handler(self):
        if self.flag:
            self.label.clear()
        else:
            self.label.setText("버튼 클릭")
        self.flag = not self.flag
        return

app = QApplication(sys.argv)
mywindow = window()
mywindow.show()
app.exec_()
