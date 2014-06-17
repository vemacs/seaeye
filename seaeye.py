# just a test
import os
from archive import Archiver
from build import ShellBuilder
from vcs import GitVCS

workspace = os.path.join(".", "workspace")
archive = os.path.join(".", "archive")

os.mkdir(workspace)
os.mkdir(archive)

git = GitVCS(os.path.join(".", "workspace"), "https://github.com/vemacs/LoadControl.git")
git.copy()
git.update()

maven = ShellBuilder("mvn clean install", os.path.join(".", "workspace"))
maven.build()

archive = Archiver(os.path.join(".", "archive"), "*.jar")
archive.archive(".")