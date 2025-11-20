from estructurals.adapter.client import IClient


class Adapter(IClient):
    def __init__(self, service):
        self._service = service
        
    def method1(self):
        return self._service.method1()  
    
    def method2(self):
        return f"method2 is adapted."