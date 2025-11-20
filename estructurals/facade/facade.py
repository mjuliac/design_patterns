from estructurals.facade.subsystem import SubsystemA, SubsystemB, SubsystemC

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()
    
    def operation(self):
        self._subsystem_a.operation()
        self._subsystem_b.operation()
        self._subsystem_c.operation()