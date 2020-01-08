from tkinter import *

class UserDialog:
    _ip = ''
    _port = 0
    _nickname = ''
    _text = 'abolish'
    def __init__(self):
       pass

    @classmethod
    def show_error_box(cls, msg):
        master = Tk()
        Label(master, text=msg).grid(row=0)
        Button(master, text='OK', command=master.destroy).grid(row=1, pady=4)
        master.mainloop()


    @classmethod
    def Get_User_Input_Id(cls):

        def Get_User_IpAndPort():
            cls._ip = e1.get()
            cls._port = int(e2.get())
            # print(cls._Ip,cls._port)
            ClientWindow.destroy()


        ClientWindow = Tk()
        Label(ClientWindow,text='请输入IP').grid(row=0,column = 1)
        Label(ClientWindow, text='IP').grid(row=1)
        Label(ClientWindow, text='Port').grid(row=2)

        e1 = Entry(ClientWindow)
        e2 = Entry(ClientWindow)

        e1.grid(row=1,column=1)
        e2.grid(row=2,column=1)

        button = Button(ClientWindow)
        button.config(text='ok',command = Get_User_IpAndPort)
        button.grid(row=3, column=0)

        ClientWindow.mainloop()

    @classmethod
    def getUserNickName(cls):
        def getUserNickNameInner():
            cls._nickname = e1.get()

            ClientWindow.destroy()

        ClientWindow = Tk()
        Label(ClientWindow, text='请输入昵称').grid(row=0)
        Label(ClientWindow, text='昵称').grid(row=1)

        e1 = Entry(ClientWindow)
        e1.grid(row=1, column=1)

        button = Button(ClientWindow)
        button.config(text='ok', command=getUserNickNameInner)
        button.grid(row=2, column=0)

        ClientWindow.mainloop()

    @classmethod
    def get_text_from_user(cls):

        def get_text():
            temp = e1.get()
            master.destroy()
            if( "Ø" in temp):
                cls.show_error_box("Invalid character in expression")
            else:
                cls._text = temp

        master = Tk()
        Label(master, text="What do you want to write?").grid(row=0)
        e1 = Entry(master)
        Label(master, text="Text: ").grid(row=1)
        e1.grid(row=1, column=1)

        button = Button(master)
        button.config(text='Set', command=get_text)
        button.grid(row=2, column=0, sticky=W, pady=4)
        master.bind('<Return>', lambda event=None: button.invoke())
        master.mainloop()

if __name__ == '__main__':
    UserDialog.Get_User_Input_Id()