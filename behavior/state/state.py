from abc import ABCMeta, abstractmethod
from behavior.state.context import Context


class IState(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, context: Context):
        pass


class StateA(IState):
    def handle(self, context: Context):
        print("State A")
        context.set_state(self)
    
class StateB(IState):
    def handle(self, context: Context):
        print("State B")
        context.set_state(self)
