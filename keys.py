import curses as cr
import win


def enter():    
    check = win.Window.getch() 
    if check == 10:
        return True
    return False

