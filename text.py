import sys, time, random, threading, curses

stdscr = curses.initscr()
stdscr.keypad(True)


PREFIX = ""
KEY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


SENTENCE = [["you are a royal magician that has been sent to the dungeon to examine and find the reason of weird growling noises coming from this place. rumors are that there was some kind of a legendary dragon monster that has been imprisoned in the dungeon approximately 100 years ago by a brave unnamed hero."], 
["upon your entry to the cold and dark abyss of the dungeon, you carelessly stepped in with no reliable light source and fell into the hole  under your own legs you didn't notice. that's all you can remember."], 
["you've hit your head upon the impact with floor, and can't remember your name and your powers partially, but you still remember what you're here for. you need to defeat the source of growling noises and find the way out of this greecy place."], 
["you're trying really hard to remember at least your first name and the class of your magic."], 
["you remember now. you're <name>, the <class> magician. now you can move further upon your way out of here."], 
["you found urself in a room with a metal door and a hole that seemed to be a switch to open it. the wooden stick to actually open it is weirdly absent. the room is mostly empty. your eyes adapted to the darkness and u see that some amount of water is pouring down the walls."]]

TEXT = dict(zip(KEY, SENTENCE))


def slowprint(t):
    SPEED = 175

    for i, l in enumerate(t):
        if ENTER.is_set():
            sys.stdout.write(t[i:])
            sys.stdout.flush()
            print("")

#            ENTER.clear() #if class enterset is set: return
                        
            return

        
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/SPEED)
    print()
