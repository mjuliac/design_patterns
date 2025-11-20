import abc
from creationals.factory.product import ProductA, ProductB

class ICreator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product(self):
        pass


class CreatorA(ICreator):
    def create_product(self):
        return ProductA()
    

class CreatorB(ICreator):
    def create_product(self):
        return ProductB()