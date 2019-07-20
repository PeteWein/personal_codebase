################################################################
import scenario_generator, sys, json, os
from random import randint
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
import pdb
################################################################
def main():
    init(strip=not sys.stdout.isatty())                                 # strip out any nasty business
    cprint(figlet_format('Peter\'s Dungeon Crawl', font='starwars'))    # print the title!
    name = input('What is your name? ')
    user = InitialSetup(name)
    user.explain_rules()                                                # explain the rules of the game!
    initialpath = user.setup_path()
    cprint(figlet_format(initialpath[0], font='digital'))
    path = input('Please choose a path. \n')
    validpath = user.check_path(path, initialpath[1])
    if validpath is False:                                              # path check flow
        retrycounter = 1
        while retrycounter < 3:
            if validpath is False:                                      # confirm choice was still bad (i.e. str)
                path = input('Please try to choose a path (again). \n')
                retrycounter +=1
                validpath = user.check_path(path, initialpath[1])
                if validpath is False and retrycounter == 3:            # max retry and then exit
                    user.user_failure()
            else:
                break
    roominfo = user.randomroom(path)
    room_outcome = user.playroom(roominfo)

################################################################
class InitialSetup(object):
    def __init__(self, name):
        self.name = name
    
    def generate_scenarios(self):                       # generate scenarios json if it doesn't exist
        if not os.path.isfile('scenarios.json'):
            scenario_generator
    
    def explain_rules(self):
        print('\nWell hello there, ' + self.name + '!',end = '\n\n')
        print('This is where the rules will go', end = '.')        

    def setup_path(self):
        # set up the path
        printpath = ' '
        pathopts = randint(3,10)
        for i in range(pathopts):
            i+=1
            printpath = printpath + str(i) + ' '
        return printpath, pathopts

    def check_path(self, path, pathopts):
        # ensure we have a number
        try:
            isinstance(int(path), int)
            # ensure we have a defined path chosen
            if (int(path) >=1 and int(path) <= pathopts):     
                print('You have picked path ' + str(path), end='. \n')
                return True
            else:
                print ('You did not pick a valid path, ' + self.name, end = '. ')
                return False
        except:
            print('You did not pick a number, ' + self.name + '. I\'m a bit smarter than that.')
            return False

    def user_failure(self):
        print('You\'ve failed me for the last time, ' + self.name, end = '. '), \
        print('Let\'s try again when you want to play!')
        sys.exit()
    
    def randomroom(self, path):
        with open('scenarios.json') as json_file:  
            data = json.load(json_file)
        prevrooms = []
        room = randint(0, len(data['scenarios'])-1)             # grab a room and store the info
        while room in prevrooms:
            room = randint(0, len(data['scenarios'])-1)         # reroll room if we've seen it before
        prevrooms.append(room)
        return data['scenarios'][room]                          # return all the relevant room info

    def playroom(self, roominfo):
        i = 1                                                   # for the view!
        print(roominfo['description'], end='\n')
        for opt in roominfo['options']:
            print(str(i) + ': ' + opt, end='\n')
            i+=1
        action = input()

        return True


################################################################
if __name__ == '__main__':
    main()
################################################################
