class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state
    
    def operation(self, unique_state):
        print(f"Flyweight: Displaying shared ({self._shared_state}) and unique ({unique_state}) state.")
        

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}
    
    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = Flyweight(key)
        return self._flyweights[key]
    
    def get_flyweights_count(self):
        return len(self._flyweights)
    