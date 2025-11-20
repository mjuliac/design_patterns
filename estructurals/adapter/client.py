from  abc import ABCMeta, abstractmethod

class IClient(metaclass=ABCMeta):
    @abstractmethod
    def method1(self, data):
        pass
    
    @abstractmethod
    def method2(self):
        pass