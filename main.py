import curses as cr
import time

import class_ 
import win
import text



def Loop():
    window = win.Window()
    game = class_.GAME()
    game.scenery.scenario = class_.Scenario.CUTSCENE
    window.winstate = win.winstate.CLOSED    



Loop()


