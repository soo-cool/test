from tkinter import *
import math

class WhiteBoard:
    drawing_tool = "line"
    # Here we have the dictionary with the used colors to paint!
    # Colors = {'b': 'blue', 'r': 'red', 'g': 'green', 'o': 'orange', 'y': 'yellow', 'c': 'cyan', 'p': 'purple1',
    #           'd': 'black', 's': 'snow'}
    line_width = 2

    def __init__(self):
        self.color = 'b'
        self.init_whiteboard()
        self._init_item_button()
        self._init_color_button()
        self.init_drawing_area()
        # self.myWhiteBoard.mainloop()

    def draw_Pencil(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_line(startX,startY,endX,endY,fill=color,width=self.line_width)

    def draw_Rectangle(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_rectangle(startX,startY,endX,endY,fill=color,width=0)

    def draw_Square(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        Length_Side = ((endX - startX) + (endY - startY))/2
        self.drawing_area.create_rectangle(startX, startY, startX + Length_Side, startY + Length_Side,fill=color,width=0)

    def draw_Oval(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_oval(startX,startY,endX,endY,fill=color,width=0)

    def draw_Line(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_line(startX,startY,endX,endY,fill=color,width=self.line_width)

    def draw_Circle(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        X_Center = (startX + endX)/2
        Y_Center = (startY + endY)/2
        radius = math.sqrt((endX - startX)**2 + (endY - startY)**2) / 2
        color = msgLst[5]
        self.drawing_area.create_oval(X_Center - radius,Y_Center - radius,X_Center + radius,Y_Center + radius,fill=color,width=0)

    def draw_from_msg(self,msg):
        msgLst = msg.split()
        draw_type = msgLst[0]
        if draw_type == 'D':
            self.draw_Pencil(msgLst)
        elif draw_type == 'R':
            self.draw_Rectangle(msgLst)
        elif draw_type == 'O':
            self.draw_Oval(msgLst)
        elif draw_type == 'L':
            self.draw_Line(msgLst)
        elif draw_type == 'C':
            self.draw_Circle(msgLst)
        elif draw_type == 'S':
            self.draw_Square(msgLst)
        else:
            pass
    def show_window(self):
        self.myWhiteBoard.mainloop()

    def init_drawing_area(self):
        self.drawing_area = Canvas(self.myWhiteBoard,width = 800,height = 500,bg='white')
        self.drawing_area.place(y=50)

    def init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('900x580')

    def set_drawing_tool(self,tool):
        print(tool)
        WhiteBoard.drawing_tool = tool
    def set_color(self,color):
        print(color)
        self.color = color

    def _init_item_button(self):
        Button(self.myWhiteBoard, text='line', height=1, width=5, bg='dark goldenrod', font='Arial',
               command=lambda: self.set_drawing_tool('line')).place(x=80, y=0)
        Button(self.myWhiteBoard, text='rect', height=1, width=5, bg='saddle brown', font='Arial',
               command=lambda: self.set_drawing_tool('rectangle')).place(x=160, y=0)
        Button(self.myWhiteBoard, text='oval', height=1, width=5, bg='NavajoWhite4', font='Arial',
               command=lambda: self.set_drawing_tool('oval')).place(x=240, y=0)
        # Button(self.myWhiteBoard, text='text', height=1, width=5, bg='SteelBlue4', font='Arial',
        #        command=self.get_text_from_user).place(x=320, y=0)
        Button(self.myWhiteBoard, text='pencil', height=1, width=5, bg='DeepSkyBlue2', font='Arial',
               command=lambda: self.set_drawing_tool('pencil')).place(x=400, y=0)
        Button(self.myWhiteBoard, text='circle', height=1, width=5, bg='Turquoise2', font='Arial',
               command=lambda: self.set_drawing_tool('circle')).place(x=480, y=0)
        Button(self.myWhiteBoard, text='square', height=1, width=5, bg='CadetBlue1', font='Arial',
               command=lambda: self.set_drawing_tool('square')).place(x=560, y=0)
        Button(self.myWhiteBoard, text='eraser', height=1, width=5, bg='purple1', font='Arial',
               command=lambda: self.set_drawing_tool('eraser')).place(x=640, y=0)
        Button(self.myWhiteBoard, text='drag', height=1, width=5, bg='green', font='Arial',
               command=lambda: self.set_drawing_tool('drag')).place(x=720, y=0)

    def _init_color_button(self):
        Button(self.myWhiteBoard, height=1, width=5, bg='red',
               command=lambda: self.set_color('r')).place(x=820,y=55)
        Button(self.myWhiteBoard, height=1, width=5, bg='orange',
               command=lambda: self.set_color('o')).place(x=820, y=110)
        Button(self.myWhiteBoard, height=1, width=5, bg='yellow',
               command=lambda: self.set_color('y')).place(x=820, y=165)
        Button(self.myWhiteBoard, height=1, width=5, bg='green',
               command=lambda: self.set_color('g')).place(x=820, y=220)
        Button(self.myWhiteBoard, height=1, width=5, bg='cyan',
               command=lambda: self.set_color('c')).place(x=820, y=275)
        Button(self.myWhiteBoard, height=1, width=5, bg='blue',
               command=lambda: self.set_color('b')).place(x=820, y=340)
        Button(self.myWhiteBoard, height=1, width=5, bg='purple1',
               command=lambda: self.set_color('p')).place(x=820, y=395)
        Button(self.myWhiteBoard, height=1, width=5, bg='black',
               command=lambda: self.set_color('d')).place(x=820, y=450)
        Button(self.myWhiteBoard, height=1, width=5, bg='snow',
               command=lambda: self.set_color('s')).place(x=820, y=505)



if __name__ == '__main__':
    wb = WhiteBoard()