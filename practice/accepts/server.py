from socket import *
import threading

def server_thread():
    global count
    count += 1
    c, a = s.accept()
    print(c)
    c.send(b"Hello Client " + bytes(count))

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 0)
s.bind(('',2222))
s.listen(10)
count = 0

t = []
for i in range(4):
    t.append(threading.Thread(target=server_thread, daemon=True))
for i in range(4):
    t[i].start()

input() # 데몬 쓰레드이기 때문에, input 으로 기다리고 있지 않으면 모든 쓰레드가 즉시 종료되어버림