from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self):
        pass    
    
    
class Numero(Expression):
    def __init__(self, value):
        self.value = value
    
    def interpret(self):
        return self.value    
    
    
class Suma(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() + self.right.interpret()
    
class Resta(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() - self.right.interpret()
    
class Multiplicacion(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() * self.right.interpret()
    
class Division(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() / self.right.interpret()   
    