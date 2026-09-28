import curses as cr
from enum import Enum


class WinState(Enum):
    OPENED = 1
    CLOSED = 2


class Window:               #implement state machine like in game class
    def __init__(self):
        self.std = None
        self.state = WinState.OPENED

        self.STATES = {
                WinState.OPENED: self.opened,
                WinState.CLOSED: self.closed }


    def opened(self):
        if self.std is not None:
            return

        self.std = cr.initscr()
        cr.noecho()
        self.std.keypad(True)
        cr.cbreak()
        self.state = WinState.OPENED
    

    def closed(self):
        if self.std is not None:   #means: if window is already initialized then close it
            self.state = WinState.CLOSED
            cr.echo()
            cr.nocbreak()
            cr.endwin()
            self.std = None
    




    def printing(self, n):
        if self.std is not None:
            self.std.addstr(n)
            self.std.refresh()


    def nodelay(self, k):
        if self.std is not None:
            self.std.nodelay(k)


#    def update(self):
#        if self.std is not None:
#            self.std.refresh()


    def getch(self):
        if self.std is not None:
            return self.std.getch()


    def run(self):  
        if self.std is None:   
            self.opened()
        self.STATES[self.state]()



window = Window()

