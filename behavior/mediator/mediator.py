from abc import ABCMeta, abstractmethod
from behavior.mediator.components import Component


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def send(self, message, colleague):
        pass
    
   

class MediatorImpl(IMediator):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)
    
    def send(self, message, colleague):
        for component in self.components:
            if component != colleague:
                component.receive(message)
    