import curses as cr
import win


def enter():    
    check = win.window.std.getch() 
    if check == 10:
        return True
    return False

