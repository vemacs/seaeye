# just a test
import os
from archive import Archiver
from build import ShellBuilder
from vcs import GitVCS

workspace = os.path.join(".", "workspace")
archive = os.path.join(".", "archive")

try:
    os.mkdir(workspace)
    os.mkdir(archive)
except:
    pass

print("Attempting clone")
git = GitVCS(workspace, "https://github.com/vemacs/LoadControl.git")
git.copy()
git.update()

print("Attempting build")
maven = ShellBuilder("mvn clean install", workspace)
maven.build()

print("Attempting archive")
archiver = Archiver(os.path.join(".", "archive"), "*.jar")
archiver.archive(".")