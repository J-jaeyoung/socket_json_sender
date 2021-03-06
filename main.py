import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket
import threading

def commit():
    QApplication.processEvents()

client_sock = None



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
        # QApplication.instance().quit()
        self.close()        # Close only current window

    def hello(self):
        print("Hello button clicked!")

window2 = None
def server(sock=None):
    print("SERVER")
    # tmp_sock, c_info = sock.accept()
    # print(f"Client from {c_info[0]}:{c_info[1]}")
    global window2
    window2 = MyWindow()
    window2.show()

class OpenServer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def run(self):
        pass

    def set_ui(self):
        # Port 라벨
        port_label = QLabel("Port", self)
        port_label.move(100,20)

        # 유효한 포트가 맞는지
        status_label = QLabel("", self)
        status_label.setStyleSheet("color: red;")
        status_label.move(150,20)

        # 포트 입력
        port = QLineEdit(self)
        port.move(100,50)
        # port.textChanged[str].connect(self.onPort)

        # 윈도우 제목
        self.setWindowTitle("Socket Json Server")
        self.setGeometry(300,300,500,500)

        # 서버 시작 버튼
        btn = QPushButton("Open", self)
        btn.setGeometry(100,100,100,100)
        btn.clicked.connect(self.try_run)

        # 서버 시작 버튼
        exit_btn = QPushButton("exit", self)
        exit_btn.setGeometry(100,220,100,40)
        exit_btn.clicked.connect(self.finish)

        # 객체에 저장
        self.port = port
        self.port_label = port_label
        self.btn = btn
        self.status_label = status_label

    def finish(self):
        # QApplication.instance().exit()
        self.close()

    def onPort(self, txt):
        # print(self.port.text())
        pass

    def try_run(self):
        port = self.port.text()
        if port.isdigit():
            port = int(port)
        else:
            self.status_label.setText("Not Integer!")
            self.status_label.adjustSize()
            return
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        try:
            sock.bind(('',port))
            sock.listen(5)
            self.status_label.setStyleSheet("color: dodgerblue;")
            self.status_label.setText(f"Open Port: {port}")
            self.status_label.adjustSize()
            commit()
            # threading.Thread(target=server, args=(sock,)).start()
            server()
            # TODO
        except:
            self.status_label.setStyleSheet("color: red;")
            self.status_label.setText(f"You can't open port: {port}")
            self.status_label.adjustSize()
            return
        # self.status_label.setStyleSheet("color: green;")
        # self.status_label.adjustSize()
        return

app = QApplication(sys.argv)
window = OpenServer() # if not, maybe Garbage Collected..?
window.show()
app.exec_()