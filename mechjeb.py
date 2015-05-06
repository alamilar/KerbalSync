import tempfile
import shutil
from mod import Mod
from zipfile import ZipFile
import distutils.core
from github3 import GitHub
import urllib2
import os




class mechjeb(Mod):
    def __init__(self, path='.', git=None, repo = ("MuMech", "MechJeb2")):
        self.path=path
        if git is None:
            self.git = GitHub()
        else:
            self.git = git
        self.reponame = repo


    def preUpdate(self):
        print "Performing pre update phase"

    def update(self):
        print "Performing update"
        self.repo = self.git.repository(self.reponame[0], self.reponame[1])
        tags = [x for x in self.repo.tags()]
        file = tags[0].zipball_url
        response = urllib2.urlopen(file)
        file = response.read()
        dir = tempfile.mkdtemp()
        print dir
        x = open(dir + '/mechjeb.zip', 'w')
        x.write(file)
        x.close()
        with ZipFile(dir + '/mechjeb.zip', 'r') as zip:
            zip.extractall(path=dir+ '/mechjeb')
        for root, dirs, files in os.walk(dir + '/mechjeb/'):
            for y in dirs:
                mariusz = os.path.join(root, y)
                os.rename(mariusz, 'MechJeb2')
        distutils.dir_util.copy_tree(dir + '/mechjeb/', self.path)
        shutil.rmtree(dir)
        print "Update phase completed"


    def postUpdate(self):
        print "Performing post update phase"
        print "Mod update completed"
