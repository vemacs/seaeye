import fnmatch
import os


class Archiver():
    def __init__(self, archivedir, pattern):
        self.archivedir = archivedir
        self.pattern = pattern

    def archive(self, workspace):
        for match in self.get_recursive_matches(workspace, self.pattern):




    def get_recursive_matches(self, dir, pattern):
        matches = []
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))
        return matches
