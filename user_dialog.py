from tkinter import *

class UserDialog:
    _ip = '127.0.0.1'
    _port = 1212

    def __init__(self):
       pass


    @classmethod
    def Get_User_Input_Id(cls):
        def Get_User_IpAndPort():
            cls._Ip = e1.get()
            cls._port = int(e2.get())
            # print(cls._Ip,cls._port)
            ClientWindow.destroy()
        ClientWindow = Tk()
        Label(ClientWindow,text='请输入IP').grid(row=0)
        Label(ClientWindow, text='IP').grid(row=1)
        Label(ClientWindow, text='Port').grid(row=2)

        e1 = Entry(ClientWindow)
        e2 = Entry(ClientWindow)

        e1.grid(row=1,column=1)
        e2.grid(row=2,column=1)

        button = Button(ClientWindow)
        button.config(text='ok',command = Get_User_IpAndPort())
        button.grid(row=3, column=0)

        ClientWindow.mainloop()

if __name__ == '__main__':
    UserDialog.Get_User_Input_Id()