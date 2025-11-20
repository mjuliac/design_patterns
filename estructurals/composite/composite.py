from estructurals.composite.component import Component

class Composite(Component):
    def __init__(self):
        self._children = []
    
    def add(self, component: Component):
        self._children.append(component)
        
    def remove(self, component: Component):
        self._children.remove(component)
        
    def operation(self):
        print("Result of operation in Composite")
        for child in self._children:
            child.operation()