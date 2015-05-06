import tempfile
import shutil
from zipfile import ZipFile
import distutils.core

from github3 import GitHub

from mod import Mod


class mks(Mod):
    def __init__(self, path='.', git=None, repo = ("BobPalmer", "MKS")):
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
        dir = tempfile.mkdtemp()
        self.repo = self.git.repository(self.reponame[0], self.reponame[1])
        releases = [x for x in self.repo.releases()]
        assets = [x for x in releases[0].assets()]
        print "Got mod, version ",
        print assets[0]
        print "Downloading mod"
        assets[0].download(path=dir + "/mks.zip")
        print"Downloaded succesfully"
        with ZipFile(dir + '/mks.zip', 'r') as zip:
            zip.extractall(path=dir+ '/mks')
        distutils.dir_util.copy_tree(dir + '/mks/GameData', self.path)
        shutil.rmtree(dir)
        print "Update phase completed"


    def postUpdate(self):
        print "Performing post update phase"
        print "Mod update completed"
