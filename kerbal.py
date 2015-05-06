from github3 import GitHub
from mks import mks
import ConfigParser
import os
from kas import kas
from mechjeb import mechjeb


def ConfigSectionMap(section, config):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


def readConfig():
    config = ConfigParser.ConfigParser()
    if os.path.isfile('config.ini'):
        try:
            config.read('config.ini')
            path = ConfigSectionMap('Config', config)['path']
            return path
        except IOError as ex:
            print 'Blad w otwieraniu pliku'
    else:
        path = raw_input('Podaj pelna sciezke do katalogu GameData\r\n np. C:\\Program Files\\Kerbal\\GameData\\ > ')
        x = open('config.ini', 'w')
        config.add_section('Config')
        config.set('Config', 'path', path)
        config.write(x)
        x.close()
        return path

def mks():
    x = mks(path=readConfig())
    x.preUpdate()
    x.update()
    x.postUpdate()

def mechjeb():
    x = mechjeb(path=readConfig())
    x.preUpdate()
    x.update()
    x.postUpdate()

def kas():
    x = kas(path=readConfig())
    x.preUpdate()
    x.update()
    x.postUpdate()

def clear():
    print '\033c';

def cancel():
    exit()

option = (1, 2, 3, 4)
function = [mechjeb, kas, mks, cancel]
while True:
    print 'Select option'
    print 'Mechjeb [1]'
    print 'Kerbal Attachement System [2]'
    print 'Modular Kolonization System [3]'
    print 'Exit [4]'
    choice = raw_input('> ')
    if int(choice) in option:
        function[int(choice)-1]()
    clear()