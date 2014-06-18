import fnmatch
import os
from shutil import copy2

class Archiver():
    def __init__(self, archivedir, pattern):
        self.archivedir = archivedir
        self.pattern = pattern

    def archive(self, workspace):
        vfile = os.path.join(self.archivedir, "VERSION")
        try:
            with open(vfile) as ver:
                version = int(ver.readline())
        except:
            version = 0
        version += 1
        with open(vfile, "w+") as ver:
            ver.write(str(version))
        storage = os.path.join(self.archivedir, str(version))
        os.mkdir(storage)
        for match in self.get_recursive_matches(workspace, self.pattern):
            with open(os.path.join(storage, os.path.splitext(os.path.basename(match))[0] + ".sha1"), "w+") as hashfile:
                hashfile.write(self.sha1OfFile(match))
            copy2(match, storage)

    def get_recursive_matches(self, dir, pattern):
        matches = []
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))
        return matches

    def sha1OfFile(self, filepath):
        import hashlib
        with open(filepath, 'rb') as f:
            return hashlib.sha1(f.read()).hexdigest()
