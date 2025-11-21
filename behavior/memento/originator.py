from abc import ABCMeta, abstractmethod
from behavior.memento.memento import Memento

class IOriginator(metaclass=ABCMeta):
     
     @abstractmethod
     def set_state(self, state):
         pass
     
     @abstractmethod
     def create_memento(self):
         pass
     
     @abstractmethod
     def set_memento(self, memento):
         pass
     
     
class Originator(IOriginator):
    def __init__(self, state):
        self.state = state
        
    def set_state(self, state):
        print(f"Originator set state: {state}")
        self.state = state
        
    def create_memento(self):
        print("Originator create memento")
        return Memento(self.state)
    
    def set_memento(self, memento):
        state = memento.get_sate()
        print(f"Originator state after restoring memento")
        self.state = state