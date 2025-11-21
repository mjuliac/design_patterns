from abc import ABCMeta, abstractmethod

class IVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit_element_a(self, element_a):
        pass
    
    @abstractmethod
    def visit_element_b(self, element_b):
        pass


class VisitorA(IVisitor):
    def visit_element_a(self, element_a):
        print("Visitor A visits Element A")
    
    def visit_element_b(self, element_b):
        print("Visitor A visits Element B")
    

class VisitorB(IVisitor):
    def visit_element_a(self, element_a):
        print("Visitor B visits Element A")
    
    def visit_element_b(self, element_b):
        print("Visitor B visits Element B")

