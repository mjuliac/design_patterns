from behavior.command.command import ICommand


class Invocator:
    def __init__(self, command:ICommand):
        self.command = command
    
    def execute(self):
        self.command.execute()  