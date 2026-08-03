import threading, re, time, sys
from enum import Enum, auto




class GAME():

    def __init__(self):
        self.state = STATE.MENU 
        self.running = True
#        self.inventory = False

    self.STATES= {
        State.MENU: self.menu
        State.PLAY: self.play
        State.INV: self.inv
        State.EXT: self.ext         }


    def run(self):
        while self.state != STATE.EXT:
            self.states[self.state]()


    def cmd(self, cmd):             #all game commands
        cmd = input(">")

        if cmd == 'play':
            self.state = State.PLAY
        elif cmd == 'exit':
            self.running = False
#        elif cmd == inv:
#            self.inventory = True
        else:
            print("wrong!")




#class ROOM():

#class ENEMY():

#class OBJ():

#class PLAYER():
