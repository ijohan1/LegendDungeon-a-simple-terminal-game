import threading, re, time, sys
from enum import Enum, auto
import curses as cr

import text
import win
import plot





class Scenario(Enum):
    CUTSCENE = 0
    ACTION = 1
    OTHER = 2


class SCENERY():
    def __init__(self):
        self.scenario = Scenario.CUTSCENE

        self.SCENARIOS = {
            Scenario.CUTSCENE: self.cutscene,
            Scenario.ACTION: self.action,
            Scenario.OTHER: self.other  }
    
    def cutscene(self):
        return plot.s1

    def action(self):
        return plot.s2

    def other(self):
        return plot.s3




class State(Enum):
    EXT = 0
    INPUT = 1
    OUTPUT = 2


class GAME():

    def __init__(self):
        self.state = State.OUTPUT
        self.running = True

        self.scenery = SCENERY()

        self.STATES = {
            State.EXT: self.ext,
            State.INPUT: self.input,
            State.OUTPUT: self.output }
        
    def ext(self):
        cr.endwin()
        self.running = False

    def input(self):
        text.Input()

    def output(self):
        text.Output(self.scenery.scenario)

    def Run(self):
        self.STATES[self.state]()




#class ROOM():

#class ENEMY():

#class OBJ():

#class PLAYER():
