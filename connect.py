import socket
from user_dialog import UserDialog
import time

class Connection:
    def __init__(self):
        UserDialog.Get_User_Input_Id()
        self.host = UserDialog._ip
        self.port = UserDialog._port
        print(self.host, self.port)

        self.sock = socket.socket()
        self.sock.connect((self.host,self.port))
        data = self.sock.recv(3).decode()
        print(data)

        usernames = self.sock.recv(1024).decode('utf-8')
        print(usernames)
        userList = usernames.split()

        while True:
            UserDialog.getUserNickName()
            self.nickname = UserDialog._nickname
            if self.nickname in userList:
                UserDialog.show_error_box('用户名已存在，请换一个')
            else:
                break

        self.sock.sendall((self.nickname.encode('utf-8')))

    def receive_msg(self):
        while True:
            time.sleep(0.1)
            data = self.sock.recv(1).decode('ISO-8859-1')
            if data == 'ß':
                # print('ß')
                continue
            else:
                pass

    def send_message(self, msg):
        msg = ' '.join(map(str, msg))
        msg = msg + " Ø"
        try:
            msg = msg.encode('ISO-8859-1')
            self.sock.send(msg)
        except UnicodeEncodeError:
            pass

if __name__ == '__main__':
    conn = Connection()
    conn.receive_msg()
    print('start')