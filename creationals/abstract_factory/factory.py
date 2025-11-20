import abc
from creationals.abstract_factory.products import ProductA, ProductB, ProductA1, ProductB1

class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self):
        pass
    
    @abc.abstractmethod
    def create_product_b(self):
        pass
    
    
class FactoryA(AbstractFactory):
    def create_product_a(self):
        return ProductA()
    
    def create_product_b(self):
        return ProductB()
    

class FactoryB(AbstractFactory):
    def create_product_a(self):
        return ProductA1()
    
    def create_product_b(self):
        return ProductB1()