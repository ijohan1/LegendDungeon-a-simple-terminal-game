from enum import Enum, auto
import curses as cr

import text
import win
import plot





class Scenarios(Enum):
    CUTSCENE = 0
    ACTION = 1
    OTHER = 2


class SCENERY:    
    def __init__(self):
        self.state = Scenarios.CUTSCENE

        self.SCENARIOS = {                     #methods list to use to according state
            Scenarios.CUTSCENE: self.cutscene,
            Scenarios.ACTION: self.action,
            Scenarios.OTHER: self.other  }
    

    def cutscene(self):
            text.slowprint(plot.s1)   #stays as it is


    def action(self):
             text.slowprint(plot.s2)            #needs to summon cmd prompt


    def other(self):
            return plot.s3   #do other stuff that may be planned for future




class mode(Enum):
    EXT = 0
    INPUT = 1
    OUTPUT = 2


class GAME:

    def __init__(self):
        self.state = mode.OUTPUT
        self.running = True

        self.scenery = SCENERY()   

        self.STATES = {
            mode.EXT: self.ext,
            mode.INPUT: self.input,
            mode.OUTPUT: self.output }
        

    def ext(self):
        self.running = False
        cr.endwin()

    def input(self):
        text.Input()  

    def output(self):
        self.scenery.action()

    def Run(self):
        self.STATES[self.state]() #calls the method according to the state of class




#class ROOM():

#class ENEMY():

#class OBJ():

#class PLAYER():
