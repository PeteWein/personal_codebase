################################################################
import scenario_generator, sys, json, time
from os import path, system, name
from random import randint
from colorama import init
from pyfiglet import figlet_format
import pdb
################################################################
"""
TODO:
-add more flavor text
-add scenario creative content (in the scenario generator script)
-either encode file (so users can't see it) or ensure script doesn't output a file
-add in rules explanation
-add keyword matching (help, exit)
-add home screen
-add ascii art for each room (?)

"""
################################################################
def main(initial):
    while initial is True:
        InitialSetup('start').title_screen()
        name = input('What is your name?\n')
        user = InitialSetup(name)
        data = user.generate_scenarios()                                    # bring in the data
        # user.explain_rules()                                                # explain the rules of the game!
        initialpath = user.setup_path()
        print(figlet_format(initialpath[0], font='digital'))
        path = input('Please choose a path. \n')
        validpath = user.check_path(path, initialpath[1])    
        if validpath is False:                                              # path check flow
            user.retry_flow(user, validpath, initialpath)
        roominfo = user.randomroom(data)
        outcome = user.playroom(user, roominfo)                             # determine outcome
        while outcome is True and roominfo['id'] != 1:                      # continue playing loop
            continuepath = user.setup_path()
            input('Press Enter to continue exploring the dungeon...\n')     # allow user to read results
            user.clearscreen()
            print(figlet_format(continuepath[0], font='digital'))
            path_text = randint(0, len(data['flavor_moving'])-1)            # funny flavor text
            print(data['flavor_moving'][path_text], end='\n')
            path = input()
            validpath = user.check_path(path, continuepath[1])    
            if validpath is False:                                          # path check flow
                user.retry_flow(user, validpath, continuepath)
            roominfo = user.randomroom(data, False)
            outcome = user.playroom(user, roominfo)                         

        if outcome is True and roominfo['id'] == 1:                         # you win!
            print(figlet_format('Congrats!\n You have won!'))
        else:                                                               # you lose
            print(figlet_format('You have died.'))
        choice = input('Would you like to play again?\n 1: Yes \n 2: No\n')
        if int(choice) == 1:                                                # continue if you want to
            user.clearscreen()
        else:                                                               # break out if not
            initial = False
            sys.exit()
            


################################################################
class InitialSetup(object):
    def __init__(self, name):
        self.name = name
    
    def clearscreen(self):   
        if name == 'nt':                                                    # for windows 
            _ = system('cls') 
        else:                                                               # for mac and linux(here, os.name is 'posix') 
            _ = system('clear') 
    
    def generate_scenarios(self):                                           # generate scenarios
        data = scenario_generator.main()
        return data
    
    def title_screen(self):
        init(strip=not sys.stdout.isatty())                                 # strip out any nasty business
        print(figlet_format('Peter\'s Dungeon Crawl', font='starwars'))     # title
        InitialSetup(self).explain_rules()
        st = input('\tPress ENTER to continue, EXIT to quit\n')
        if st.lower() == 'exit':                                            # opt to exit at title screen
            sys.exit()
        InitialSetup(self).clearscreen()

    def explain_rules(self):
        print('Your objective is to find the treasure hiding.', end = '\n'), 
        print('somewhere in this dungeon and escape. Be careful, as it ', end = '\n'),
        print('can be a very dangeous place. Good luck...', end='\n\n')

    def setup_path(self):                                                   # set up doors for display
        printpath = ' '
        pathopts = randint(3,9)
        for i in range(pathopts):
            i+=1
            printpath = printpath + str(i) + ' '
        return printpath, pathopts

    def check_path(self, path, pathopts):
        try:                                                                # ensure we have a number
            isinstance(int(path), int)                                      # ensure we have a defined path chosen
            if (int(path) >=1 and int(path) <= pathopts):
                print('You have picked path ' + str(path), end='. \n')
                return True
            else:
                print ('You did not pick a valid path, ' + self.name, end = '. ')
                return False
        except:
            print('You did not pick a number, ' + self.name + '. I\'m a bit smarter than that.')
            return False

    def retry_flow(self, user, validpath, initialpath):                     # make sure user picks one of the opts
        retrycounter = 1
        while retrycounter < 3:
            if validpath is False:                                          # confirm choice was still bad (i.e. str)
                path = input('Please try to choose a valid option. \n')
                retrycounter +=1
                validpath = user.check_path(path, initialpath[1])
                if validpath is False and retrycounter == 3:                # max retry and then exit
                    user.user_failure()
            else:
                return validpath is True

    def user_failure(self):                                                 # too many failures causes game to quit
        print('You\'ve failed me for the last time, ' + self.name, end = '. '), \
        print('Let\'s try again when you want to play!')
        time.sleep(2)
        sys.exit()
    
    def randomroom(self, data, firstroom = True):
        prevrooms = []
        i = 1
        if firstroom is False:                                              # ensure you can't get the winner first round
            i = 0
        room = randint(i, len(data['scenarios'])-1)                         # grab a room and store the info
        while room in prevrooms:
            room = randint(0, len(data['scenarios'])-1)                     # reroll room if we've seen it before
        prevrooms.append(room)
        return data['scenarios'][room]                                      # return all the relevant room info

    def playroom(self, user, roominfo):
        i = 1                                                               # for user option viewability (1: X, 2: Y, etc.)
        print(roominfo['description'], end='\n')
        for opt in roominfo['options']:
            print(str(i) + ': ' + opt, end='\n')
            i+=1
        action = input()
        valid_choice = user.check_input(action, (i-1))                      # ensure they picked something
        retry = 1
        while valid_choice is False and retry < 3:                          # retry flow
            action = input()
            valid_choice = user.check_input(action, (i-1))                  # 3 trys before failure
            if retry == 3:
                user.user_failure()
            retry += 1
        print(roominfo['outcome'][int(action)-1])                           # show the outcome
        return roominfo['result'][int(action)-1]                            # store the results

    def check_input(self, input, max):                                      # check user inputs for validity
        try:
            isinstance(int(input), int)
            # ensure we have a defined path chosen
            if (int(input) >=1 and int(input) <= max):     
                return True
            else:
                print ('You did not pick a valid option, ' + self.name, end = '.\n')
                return False
        except:
            print ('You did not pick a valid option, ' + self.name, end = '.\n')
            return False



################################################################
if __name__ == '__main__':
    initial = True
    main(initial)
################################################################
