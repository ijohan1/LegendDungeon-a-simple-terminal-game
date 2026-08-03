from text import slowprint
from class_ import GAME, cmd, STATE


def startLogo():
    NAME = r"""
----------------------------------------------------------------
 __                      _ ____                          
|  |   ___ ___ ___ ___ _| |    \ _ _ ___ ___ ___ ___ ___ 
|  |__| -_| . | -_|   | . |  |  | | |   | . | -_| . |   |
|_____|___|_  |___|_|_|___|____/|___|_|_|_  |___|___|_|_|
          |___|                         |___|             
          
----------------------------------------------------------------"""
    print(NAME)


game = GAME()
while game.running():
    command = input(">")
    game.cmd(command)


def sequence(): #rewrite (use another input library)
    i = 0

    while i <=5:
        slowprint(SENTENCE[i][0])

        while not ENTER.is_set():
            time.sleep(0.1)
        ENTER.wait()
        ENTER.clear()
        i+=1

#поки слоупрінт іде, нехай він буде лише одним потоком

def cmd():
    command = input(">")
    if command == 'start':
       state.PLAY() 
    elif command == 'quit':
       state.EXT() 
#    elif command == 'inv':
#        inventory() #inventory func. add in future
    else: 
        print('wrong!')


def loop(): #check how can u actually use the class with states in another function
    if game.state == STATE.MENU:
        startLogo()
        cmd()


    

