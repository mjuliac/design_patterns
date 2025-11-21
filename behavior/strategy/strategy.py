from abc import ABCMeta, abstractmethod


class IStrategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategyA(IStrategy):
    def execute(self):
        print("Executing strategy A")
    

class ConcreteStrategyB(IStrategy):
    def execute(self):
        print("Executing strategy B")
    