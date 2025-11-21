from abc import ABCMeta, abstractmethod


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, publisher):
        pass
    
class ConcreteObserverA(IObserver):
    def update(self, publisher):
        if publisher.get_state() == 1:
            print("Concrete observer A: React to event")
            
class ConcreteObserverB(IObserver):
    def update(self, publisher):
        if publisher.get_state() == 0:
            print("Concrete observer B: React to event")