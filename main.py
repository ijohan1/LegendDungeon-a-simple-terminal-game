import curses as cr
#import time

import class_ 
import win
import text



def Loop():
    game = class_.GAME()
    game.scenery.state = class_.Scenarios.CUTSCENE
    while game.running:
        win.window.Run()
        game.Run()
    win.window.winstate = win.winstate.CLOSED    
    win.window.closed()



Loop()
