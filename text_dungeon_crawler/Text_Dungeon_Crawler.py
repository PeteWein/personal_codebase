################################################################
from random import randint
import sys, json
import pdb
################################################################
def main():
    name = input('What is your name? ')
    print('Well hello there, ' + name + '!',end = '\n')
    user = InitialSetup(name)
    initialpath = user.setup_path()
    print(initialpath[0])
    path = input('Please choose a path.\n')
    validpath = user.check_path(path, initialpath[1])
    if validpath is False:                                              # path check flow
        retrycounter = 1
        while retrycounter < 3:
            if validpath is False:                                      # confirm choice was still bad (i.e. str)
                path = input('Please try to choose a path (again).\n')
                retrycounter +=1
                validpath = user.check_path(path, initialpath[1])
                if validpath is False and retrycounter == 3:            # max retry and then exit
                    user.user_failure()
            else:
                print('I see you can follow instructions. Moving on!')
    roominfo = user.randomroom(path)
    print(roominfo)

################################################################
class InitialSetup(object):
    def __init__(self, name):
        self.name = name
    
    def setup_path(self):
        # set up the path
        printpath = '||'
        pathopts = randint(3,10)
        for i in range(pathopts):
            i+=1
            printpath = printpath + str(i) + '||'
        return printpath, pathopts

    def check_path(self, path, pathopts):
        # ensure we have a number
        try:
            isinstance(int(path), int)
            # ensure we have a defined path chosen
            if (int(path) >=1 and int(path) <= pathopts):     
                print('You have picked path ' + str(path), end='.')
                return True
            else:
                print ('You did not pick a valid path, ' + self.name, end = '. ')
                return False
        except:
            print('You did not pick a number, ' + self.name + '. I\'m a bit smarter than that.')
            return False

    def user_failure(self):
        print('You\'ve failed me for the last time, ' + self.name, end = '. '), \
        print('The program will now abort.')
        sys.exit()
    
    def randomroom(self, path):
        with open('C:/Users/Home/Desktop/git_repo/python/scenarios.json') as json_file:  
            data = json.load(json_file)
        room = randint(0, len(data['scenarios'])-1)             # grab a room and store the info
        des = data['scenarios'][room]['description']
        numopts = len(data['scenarios'][room]['optinfo'])
        return room, des, numopts


################################################################
if __name__ == '__main__':
    main()
################################################################
