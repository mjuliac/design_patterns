import abc

class IProduct(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def descripttion(self) -> str:
        pass
    
    
class ProductA(IProduct):
    def descripttion(self) -> str:
        return "This is Product A"
    
    
class ProductB(IProduct):
    def descripttion(self) -> str:
        return "This is Product B"