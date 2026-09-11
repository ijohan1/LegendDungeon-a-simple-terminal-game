import curses as cr
from enum import Enum, auto


#def window():
#    global std
#    std = cr.initscr()
#    cr.noecho()
#    std.keypad(true)
#    cr.cbreak()

class winstate(Enum):
    OPENED = 1
    CLOSED = 2


class Window():
    def __init__(self):
        self.std = None
        self.state = winstate.OPENED

        self.STATES = {
                winstate.OPENED: self.opened,
                winstate.CLOSED: self.closed }


    def opened(self):
        if self.std is not None:
            return

        self.std = cr.initscr()
        cr.noecho()
        self.std.keypad(True)
        cr.cbreak()
        self.state = winstate.OPENED
    
    def closed(self):
        if self.std is not None:
            self.state = winstate.CLOSED
            cr.endwin()

window = Window()

