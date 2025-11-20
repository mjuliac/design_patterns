from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self, request):
        pass
    
    @abstractmethod
    def set_next(self, handler):
        pass
    
class Handler(IHandler):
        
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    
    def handle(self, request):
        handled = self._handle(request)
        if not handled:
            self._next_handler.handle(request)              
   
    def _handle(self, request):
        pass
    
class ConcreteHandlerA(Handler):
    def _handle(self, request):
        if request > 0 and request <= 10:
            print(f"ConcreteHandlerA handled the request {request}")
            return True
        return False
    
class ConcreteHandlerB(Handler):
    def _handle(self, request):
        if request > 10 and request <= 20:
            print(f"ConcreteHandlerB handled the request {request}")
            return True
        return False
        
class ConcreteHandlerC(Handler):
    def _handle(self, request):
        if request > 20 and request <= 30:
            print(f"ConcreteHandlerC handled the request {request}")
            return True
        return False
        
class DefaultHandler(Handler):
    def _handle(self, request):
        print(f"DefaultHandler handled the request {request}")
        return True
        