class Publisher:
    def __init__(self):
        self._observers = []
        self.state = None

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
            
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.notify()
