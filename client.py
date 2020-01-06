import socket
from user_dialog import UserDialog

class Connection:
    def __init__(self):
        UserDialog.Get_User_Input_Id()
        self.host = UserDialog._ip
        self.port = UserDialog._port
        self.sock = socket.socket()
        self.sock.connect((self.host,self.port))


if __name__ == '__main__':
    conn = Connection
    print('start')