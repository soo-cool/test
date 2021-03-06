import socket
import time
from user_dialog import UserDialog


class Connection:
    def __init__(self):
        UserDialog.Get_User_Input_Id()
        self.host = UserDialog._ip
        self.port = UserDialog._port
        print(self.host,self.port)

        self.sock = socket.socket()
        self.sock.connect((self.host,self.port))
        data = self.sock.recv(3).decode()
        print(data)

        UserDialog.getUserNickName()
        self.nickname = UserDialog._nickname

        self.sock.sendall((self.nickname.encode('utf-8')))

    def start(self):
        while True:
            time.sleep(0.1)
            pass

if __name__ == '__main__':
    conn = Connection()
    conn.start()
    print('start')

