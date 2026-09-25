import time, random 
import curses as cr

import keys
import win
import class_


#def startLogo():
#    NAME = r"""
#----------------------------------------------------------------
#|  |   ___ ___ ___ ___ _| |    \ _ _ ___ ___ ___ ___ ___ 
#|  |__| -_| . | -_|   | . |  |  | | |   | . | -_| . |   |
#|_____|___|_  |___|_|_|___|____/|___|_|_|_  |___|___|_|_|
#          |___|                         |___|             
#          
#----------------------------------------------------------------"""
#    win.Win.printing(NAME)
#    win.Win.printing("\n")
#


#PREFIX = ""
#KEY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #append automatically with more text amount


#SENTENCE = ["you are a royal magician that has been sent to the dungeon to examine and find the reason of weird growling noises coming from this place. rumors are that there was some kind of a legendary dragon monster that has been imprisoned in the dungeon approximately 100 years ago by a brave unnamed hero. ", 
#"upon your entry to the cold and dark abyss of the dungeon, you carelessly stepped in with no reliable light source and fell into the hole  under your own legs you didn't notice. that's all you can remember. ", 
#"you've hit your head upon the impact with floor, and can't remember your name and your powers partially, but you still remember what you're here for. you need to defeat the source of growling noises and find the way out of this greecy place. ", 
#"you're trying really hard to remember at least your first name and the class of your magic. ", 
#"you remember now. you're <name>, the <class> magician. now you can move further upon your way out of here. ", 
#"you found urself in a room with a metal door and a hole that seemed to be a switch to open it. the wooden stick to actually open it is weirdly absent. the room is mostly empty. your eyes adapted to the darkness and u see that some amount of water is pouring down the walls. "]
#

#SENTENCE = ["hi henlo. ",
#"hi henlo. ",
#"hi henlo. ",
#"hi henlo. ",
#"there you go, poetry. "]
#


# 1st enter for skip, 2nd enter for continue. 
def slowprint(t): 
    SPEED = 175
    for i, l in enumerate(t): # the issue with code
        if keys.enter() == True:
            win.Win.printing(t[i:])
            win.Win.update()


            win.Win.nodelay(False)         
            while win.Win.getch() != 10: 
                pass
            win.Win.nodelay(True)


            print("")
            return
        win.Win.printing(l)
        win.Win.update()
        time.sleep(random.random()*10.0/SPEED)



def Output(p):  #rewrite!!!!!!!!!!!!!!!!!!!!!!!!!!!
    slowprint(p)

    win.window.printing("\n")
#    if keys.enter == True: why
#            cr.endwin()




def Input():
    comnd = '' 
    while True:
        win.Win.update()
        win.Win.printing("$" + comnd)
        win.Win.update()
        key = win.Win.getch()
        if key == 10:   #пішли команди внизу
            if comnd == "penis":
                win.Win.printing("\nсам такий сука")
                win.Win.getch()
            comnd = '' 
            return 
        elif 32 <= key <= 126:
            comnd += chr(key)


