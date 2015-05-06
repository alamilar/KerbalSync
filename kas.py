from mod import Mod
import urllib2
import tempfile
import shutil
from zipfile import ZipFile
import distutils.core


class kas(Mod):
    def __init__(self, path='.'):
        self.path = path

    def preUpdate(self):
        print 'Performing pre update phase'


    def update(self):
        print 'Performin update phase'
        response = urllib2.urlopen('http://kerbal.curseforge.com/ksp-mods/223900-kerbal-attachment-system-kas/files/latest')
        file = response.read()
        dir = tempfile.mkdtemp()
        x = open(dir + '/kas.zip', 'w')
        x.write(file)
        x.close()
        with ZipFile(dir + '/kas.zip', 'r') as zip:
            zip.extractall(path=dir+ '/kas')
        distutils.dir_util.copy_tree(dir + '/kas/GameData', self.path)
        shutil.rmtree(dir)
        print "Update phase completed"

    def postUpdate(self):
        print 'Performin post update phase'
        print 'Mod update completed'
