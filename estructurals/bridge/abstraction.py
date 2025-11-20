class Abstraction:
    def __init__(self, interface):
        self.interface = interface

    def operation(self):
        return f"Abstraction with {self.interface.method()}"