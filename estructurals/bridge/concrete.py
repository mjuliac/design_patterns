from estructurals.bridge.interface import Interface

class ConcreteImplementationA(Interface):
    def method(self):
        return "Concrete Implementation A"
    
class ConcreteImplementationB(Interface):
    def method(self):
        return "Concrete Implementation B"