from abc import ABCMeta, abstractmethod
from estructurals.decorator.component import IComponent


class IDecorator(IComponent, metaclass=ABCMeta):
    def __init__(self, component: IComponent):
        self._component = component
    
    @abstractmethod
    def operation(self):
        self._component.operation()
        
class Decorator(IDecorator):
    def operation(self):
        super().operation()
        self.add_behavior()
        
    def add_behavior(self):
        print("Add behavior to component")
        