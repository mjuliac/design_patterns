import abc

class IProductA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def descripttion(self) -> str:
        pass
    

class IProductB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def descripttion(self) -> str:
        pass

class ProductA(IProductA):
    def descripttion(self) -> str:
        return "This is Product A from Factory A"
    
    
class ProductB(IProductA):
    def descripttion(self) -> str:
        return "This is Product B from Factory A"
    
    
class ProductA1(IProductB):
    def descripttion(self) -> str:
        return "This is Product A1 from Factory B"
    
    
class ProductB1(IProductB):
    def descripttion(self) -> str:
        return "This is Product B1 from Factory B"
    