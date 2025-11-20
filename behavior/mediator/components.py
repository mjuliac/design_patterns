class Component:
    def __init__(self, mediator):
        self.mediator = mediator    
    
    def send(self, message):
        self.mediator.send(message, self)
    
    def receive(self, message):
        pass


class ComponentA(Component):
    def receive(self, message):
        print(f"Component A received message: {message}")


class ComponentB(Component):
    def receive(self, message):
        print(f"Component B received message: {message}")
