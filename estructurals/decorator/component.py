from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass
    
    
class Component(IComponent):
    def operation(self):
        print("Operation in Concrete Component")