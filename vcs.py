from subprocess import call
import subprocess

class VCS():
    def __init__(self, workspace):
        self.workspace = workspace

    def copy(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

class GitVCS(VCS):
    # How2branches?
    def __init__(self, workspace, url):
        VCS.__init__(self, workspace)
        self.url = url

    def copy(self):
        # I think we should be safe with shell=False
        call(["git", "clone", self.url], cwd=self.workspace)

    def update(self):
        p = subprocess.Popen(["git", "pull"], cwd=self.workspace)
        for line in p.stdout.readlines():
            if line.startswith("Already up-to-date."):
                return False
        return True