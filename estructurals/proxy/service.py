from abc import ABCMeta, abstractmethod

class IService(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass
    
    
class Service(IService):
    def operation(self):
        print("Service operation")
