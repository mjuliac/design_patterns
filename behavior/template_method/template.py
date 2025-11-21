from abc import ABCMeta, abstractmethod

class ITemplate(metaclass=ABCMeta):

    def template_method(self):
        self.step1()
        self.step2()

    @abstractmethod
    def step1(self):
        pass
    
    @abstractmethod
    def step2(self):
        pass

    