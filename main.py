from tkinter import *


class Cross:

    def st_nafa(self, event):
        self.nafa()

    def nafa(self):
        self.check()
        self.st_game()

        self.root.after(10, self.nafa)

    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac')
        self.root.minsize(500, 500)
        self.root.resizable(False, False)

        self.winner = False
        self.win_player = ''
        self.btn_restart = Button(self.root, text='Restart', font=('Ubuntu', 15))

        self.grid1 = ''
        self.grid2 = ''
        self.grid3 = ''
        self.grid4 = ''
        self.grid5 = ''
        self.grid6 = ''
        self.grid7 = ''
        self.grid8 = ''
        self.grid9 = ''

        self.next = 0

        self.cr = True
        self.ci = False

        self.TextForUser = Label(self.root, text='X - First O - second', font=('Ubuntu', 20))
        self.TextForUser.grid(row=0, column=2)

        self.Clear = Button(self.root, text='Start', font=('Ubuntu', 15))
        self.Clear.grid(row=1, column=2)
        self.Clear.bind('<Button-1>', self.st_nafa)

        self.btn1 = Button(self.root, height=10, width=20)
        self.btn2 = Button(self.root, height=10, width=20)
        self.btn3 = Button(self.root, height=10, width=20)
        self.btn4 = Button(self.root, height=10, width=20)
        self.btn5 = Button(self.root, height=10, width=20)
        self.btn6 = Button(self.root, height=10, width=20)
        self.btn7 = Button(self.root, height=10, width=20)
        self.btn8 = Button(self.root, height=10, width=20)
        self.btn9 = Button(self.root, height=10, width=20)

        self.btn1.grid(row=2, column=1, sticky='ew')
        self.btn2.grid(row=2, column=2, sticky='we')
        self.btn3.grid(row=2, column=3, sticky='ew')

        self.btn4.grid(row=3, column=1, sticky='ew')
        self.btn5.grid(row=3, column=2, sticky='we')
        self.btn6.grid(row=3, column=3, sticky='ew')

        self.btn7.grid(row=4, column=1, sticky='ew')
        self.btn8.grid(row=4, column=2, sticky='we')
        self.btn9.grid(row=4, column=3, sticky='ew')

        self.btn1.bind('<Button-1>', self.draw1)
        self.btn2.bind('<Button-1>', self.draw2)
        self.btn3.bind('<Button-1>', self.draw3)

        self.btn4.bind('<Button-1>', self.draw4)
        self.btn5.bind('<Button-1>', self.draw5)
        self.btn6.bind('<Button-1>', self.draw6)

        self.btn7.bind('<Button-1>', self.draw7)
        self.btn8.bind('<Button-1>', self.draw8)
        self.btn9.bind('<Button-1>', self.draw9)

        self.cross = PhotoImage(file='Img/Cross.gif')
        self.circle = PhotoImage(file='Img/Circle.gif')

        self.cross_lb_1 = Label(self.root, image=self.cross)
        self.cross_lb_2 = Label(self.root, image=self.cross)
        self.cross_lb_3 = Label(self.root, image=self.cross)
        self.cross_lb_4 = Label(self.root, image=self.cross)
        self.cross_lb_5 = Label(self.root, image=self.cross)
        self.cross_lb_6 = Label(self.root, image=self.cross)
        self.cross_lb_7 = Label(self.root, image=self.cross)
        self.cross_lb_8 = Label(self.root, image=self.cross)
        self.cross_lb_9 = Label(self.root, image=self.cross)

        self.circle_lb_1 = Label(self.root, image=self.circle)
        self.circle_lb_2 = Label(self.root, image=self.circle)
        self.circle_lb_3 = Label(self.root, image=self.circle)
        self.circle_lb_4 = Label(self.root, image=self.circle)
        self.circle_lb_5 = Label(self.root, image=self.circle)
        self.circle_lb_6 = Label(self.root, image=self.circle)
        self.circle_lb_7 = Label(self.root, image=self.circle)
        self.circle_lb_8 = Label(self.root, image=self.circle)
        self.circle_lb_9 = Label(self.root, image=self.circle)

    def draw1(self, event):
        self.nt()
        self.btn1.grid_forget()
        if not self.cr and self.grid1 != 'circle':
            self.cross_lb_1.grid(row=2, column=1, stick='ew')
            self.grid1 = 'cross'
            self.cr = True
        elif not self.ci and self.grid1 != 'cross':
            self.grid1 = 'circle'
            self.circle_lb_1.grid(row=2, column=1)
            self.ci = True

    def draw2(self, event):
        self.nt()
        self.btn2.grid_forget()
        if not self.cr and self.grid2 != 'circle':
            self.grid2 = 'cross'
            self.cross_lb_2.grid(row=2, column=2, stick='we')
            self.cr = True
        elif not self.ci and self.grid2 != 'cross':
            self.grid2 = 'circle'
            self.circle_lb_2.grid(row=2, column=2)
            self.ci = True

    def draw3(self, event):
        self.nt()
        self.btn3.grid_forget()
        if not self.cr and self.grid3 != 'circle':
            self.grid3 = 'cross'
            self.cross_lb_3.grid(row=2, column=3, stick='ew')
            self.cr = True
        elif not self.ci and self.grid3 != 'cross':
            self.grid3 = 'circle'
            self.circle_lb_3.grid(row=2, column=3)
            self.ci = True

    def draw4(self, event):
        self.nt()
        self.btn4.grid_forget()
        if not self.cr and self.grid4 != 'circle':
            self.grid4 = 'cross'
            self.cross_lb_4.grid(row=3, column=1, stick='ew')
            self.cr = True
        elif not self.ci and self.grid4 != 'cross':
            self.grid4 = 'circle'
            self.circle_lb_4.grid(row=3, column=1)
            self.ci = True

    def draw5(self, event):
        self.nt()
        self.btn5.grid_forget()
        if not self.cr and self.grid5 != 'circle':
            self.grid5 = 'cross'
            self.cross_lb_5.grid(row=3, column=2, stick='we')
            self.cr = True
        elif not self.ci and self.grid5 != 'cross':
            self.grid5 = 'circle'
            self.circle_lb_5.grid(row=3, column=2)
            self.ci = True

    def draw6(self, event):
        self.nt()
        self.btn6.grid_forget()
        if not self.cr and self.grid6 != 'circle':
            self.grid6 = 'cross'
            self.cross_lb_6.grid(row=3, column=3, stick='ew')
            self.cr = True
        elif not self.ci and self.grid6 != 'cross':
            self.grid6 = 'circle'
            self.circle_lb_6.grid(row=3, column=3)
            self.ci = True

    def draw7(self, event):
        self.nt()
        self.btn7.grid_forget()
        if not self.cr and self.grid7 != 'circle':
            self.grid7 = 'cross'
            self.cross_lb_7.grid(row=4, column=1, stick='ew')
            self.cr = True
        elif not self.ci and self.grid7 != 'cross':
            self.grid7 = 'circle'
            self.circle_lb_7.grid(row=4, column=1)
            self.ci = True

    def draw8(self, event):
        self.nt()
        self.btn8.grid_forget()
        if not self.cr and self.grid8 != 'circle':
            self.grid8 = 'cross'
            self.cross_lb_8.grid(row=4, column=2, stick='we')
            self.cr = True
        elif not self.ci and self.grid8 != 'cross':
            self.grid8 = 'circle'
            self.circle_lb_8.grid(row=4, column=2)
            self.ci = True

    def draw9(self, event):
        self.nt()
        self.btn9.grid_forget()
        if not self.cr and self.grid9 != 'circle':
            self.grid9 = 'cross'
            self.cross_lb_9.grid(row=4, column=3, stick='ew')
            self.cr = True
        elif not self.ci and self.grid9 != 'cross':
            self.grid9 = 'circle'
            self.circle_lb_9.grid(row=4, column=3)
            self.ci = True

    def nt(self):
        if (self.next % 2) == 0:
            self.next += 1
            self.cr = False
        else:
            self.next += 1
            self.ci = False

    def check(self):
        if self.grid1 == 'cross' and self.grid2 == 'cross' and self.grid3 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid1 == 'circle' and self.grid2 == 'circle' and self.grid3 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()
        elif self.grid4 == 'cross' and self.grid5 == 'cross' and self.grid6 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid4 == 'circle' and self.grid5 == 'circle' and self.grid6 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()
        elif self.grid7 == 'cross' and self.grid8 == 'cross' and self.grid9 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid7 == 'circle' and self.grid8 == 'circle' and self.grid9 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()
        if self.grid1 == 'cross' and self.grid4 == 'cross' and self.grid7 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid1 == 'circle' and self.grid4 == 'circle' and self.grid7 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()
        elif self.grid2 == 'cross' and self.grid5 == 'cross' and self.grid8 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid2 == 'circle' and self.grid5 == 'circle' and self.grid8 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()
        elif self.grid3 == 'cross' and self.grid6 == 'cross' and self.grid9 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid3 == 'circle' and self.grid6 == 'circle' and self.grid9 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()

        if self.grid1 == 'cross' and self.grid5 == 'cross' and self.grid9 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid1 == 'circle' and self.grid5 == 'circle' and self.grid9 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()

        if self.grid3 == 'cross' and self.grid5 == 'cross' and self.grid7 == 'cross':
            self.winner = True
            self.win_player = 'X'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.cross_lb_2.grid_forget()
            self.cross_lb_1.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_9.grid_forget()
            self.cross_lb_8.grid_forget()

            self.circle_lb_1.grid_forget()
            self.circle_lb_2.grid_forget()
            self.circle_lb_3.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_5.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_7.grid_forget()
            self.circle_lb_8.grid_forget()
            self.circle_lb_9.grid_forget()
        elif self.grid3 == 'circle' and self.grid5 == 'circle' and self.grid7 == 'circle':
            self.winner = True
            self.win_player = 'O'

            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn5.grid_forget()
            self.btn6.grid_forget()
            self.btn7.grid_forget()
            self.btn8.grid_forget()
            self.btn9.grid_forget()

            self.circle_lb_2.grid_forget()
            self.circle_lb_1.grid_forget()
            self.circle_lb_4.grid_forget()
            self.circle_lb_6.grid_forget()
            self.circle_lb_9.grid_forget()
            self.circle_lb_8.grid_forget()

            self.cross_lb_1.grid_forget()
            self.cross_lb_2.grid_forget()
            self.cross_lb_3.grid_forget()
            self.cross_lb_4.grid_forget()
            self.cross_lb_5.grid_forget()
            self.cross_lb_6.grid_forget()
            self.cross_lb_7.grid_forget()
            self.cross_lb_8.grid_forget()
            self.cross_lb_9.grid_forget()
    def st_game(self):
        self.Clear.grid_forget()
        self.btn_restart.grid(row=1, column=2)
        self.btn_restart.bind('<Button-1>', self.rs_game)
        if self.winner:
            self.TextForUser.configure(text='Winner is ' + self.win_player)
        else:
            self.TextForUser.configure(text='Waiting Winner...')

    def rs_game(self, event):
        self.winner = False
        self.win_player = ''

        self.grid1 = ''
        self.grid2 = ''
        self.grid3 = ''
        self.grid4 = ''
        self.grid5 = ''
        self.grid6 = ''
        self.grid7 = ''
        self.grid8 = ''
        self.grid9 = ''

        self.next = 0

        self.cr = True
        self.ci = False

        self.TextForUser.grid(row=0, column=2)

        self.Clear.grid(row=1, column=2)

        self.btn1.grid(row=2, column=1, sticky='ew')
        self.btn2.grid(row=2, column=2, sticky='we')
        self.btn3.grid(row=2, column=3, sticky='ew')

        self.btn4.grid(row=3, column=1, sticky='ew')
        self.btn5.grid(row=3, column=2, sticky='we')
        self.btn6.grid(row=3, column=3, sticky='ew')

        self.btn7.grid(row=4, column=1, sticky='ew')
        self.btn8.grid(row=4, column=2, sticky='we')
        self.btn9.grid(row=4, column=3, sticky='ew')

        self.cross_lb_1.grid_forget()
        self.cross_lb_2.grid_forget()
        self.cross_lb_3.grid_forget()
        self.cross_lb_4.grid_forget()
        self.cross_lb_5.grid_forget()
        self.cross_lb_6.grid_forget()
        self.cross_lb_7.grid_forget()
        self.cross_lb_8.grid_forget()
        self.cross_lb_9.grid_forget()

        self.circle_lb_1.grid_forget()
        self.circle_lb_2.grid_forget()
        self.circle_lb_3.grid_forget()
        self.circle_lb_4.grid_forget()
        self.circle_lb_5.grid_forget()
        self.circle_lb_6.grid_forget()
        self.circle_lb_7.grid_forget()
        self.circle_lb_8.grid_forget()
        self.circle_lb_9.grid_forget()


root = Tk()

core = Cross(root)

root.mainloop()
