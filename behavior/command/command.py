from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    
    @abstractmethod
    def execute(self):
        pass
    

class CommandImpl(ICommand):

    def __init__(self, receptor):
        self.receptor = receptor
    
    def execute(self):
        self.receptor.action()
