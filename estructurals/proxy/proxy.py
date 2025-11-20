from estructurals.proxy.service import IService, Service

class Proxy(IService):
    def __init__(self, service: IService=None):
        self._service = service
        
    def operation(self):
        if self._service is None:
            self._service = Service()
        return self._service.operation()
        