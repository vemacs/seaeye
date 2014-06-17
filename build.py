from subprocess import call

class Builder():
    def __init__(self, workspace):
        self.workspace = workspace

    def build(self):
        raise NotImplementedError

class ShellBuilder(Builder):
    def __init__(self, command, workspace):
        Builder.__init__(self, workspace)
        self.command = command

    def build(self):
        call(self.command.split(" "))
