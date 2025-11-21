class Context:
    def __init__(self, state=None):
        self._state = state
        
    def get_state(self):
        return self._state
    
    def set_state(self, state):
        self._state = state 

    def request(self):
        self._state.handle(self)