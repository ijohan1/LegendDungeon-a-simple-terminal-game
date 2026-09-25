import curses as cr
#import time

import class_ 
import win
import text



def Loop():
    game = class_.GAME()
    game.scenery.state = class_.Scenarios.CUTSCENE
    while game.running:
        win.Window.Run()
        game.Run()
    win.Window.winstate = win.winstate.CLOSED    
    win.Window.closed()



Loop()
