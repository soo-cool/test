import time
from threading import Thread
from connect import Connection
from whiteboard import WhiteBoard


class Client(Thread,WhiteBoard):

    def __init__(self):
        self.conn = Connection()
        Thread.__init__(self)
        WhiteBoard.__init__(self)
        self._init_mouse_event()
        self.setDaemon(True)
        self.isMouseDown = False
        self.x_pos = None
        self.y_pos = None

    def _init_mouse_event(self):
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

    def left_but_down(self,event=None):
        self.isMouseDown = True
        self.x_pos = event.x
        self.y_pos = event.y

    def left_but_up(self,event=None):
        self.isMouseDown = False
        print(event.x,event.y)

    def motion(self,event=None):
        if self.isMouseDown == True:
            msg = ('D',self.x_pos,self.y_pos,event.x,event.y,'red')
            self.conn.send_message(msg)
            self.x_pos = event.x
            self.y_pos = event.y


    def run(self):
        # print('run')aa
        while True:
            msg = self.conn.receive_msg()
            if msg == 'xxx':
                pass
            time.sleep(0.1)

if __name__ == '__main__':
    client = Client()
    print('start')
    client.start()
    client.show_window()