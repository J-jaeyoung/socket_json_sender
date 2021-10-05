from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first pyqt5")
        self.setGeometry(100,100,500,500)

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


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = MyWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
