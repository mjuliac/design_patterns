from abc import ABCMeta, abstractmethod


class IElement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ElementA(IElement):
    def accept(self, visitor):
        visitor.visit_element_a(self)
    

class ElementB(IElement):
    def accept(self, visitor):
        visitor.visit_element_b(self)
    
