import curses as cr
import time

import class_ 
import win
import text



def Loop():
    game = class_.GAME()
    game.scenery.scenario = class_.Scenario.CUTSCENE
    while game.running:
        win.window.opened()
        game.Run()
    win.window.winstate = win.winstate.CLOSED    
    win.window.closed()



Loop()
