class Caregiver:
    def __init__(self, originator):
        self.mementos = []
        self.originator = originator
        
    def backup(self):
        print(f"Caregiver saving memento state")
        self.mementos.append(self.originator.create_memento())
        
    def revert(self):
        if not len(self.mementos):
            return
        
        memento = self.mementos.pop()
        print(f"Caregiver restoring state to {memento.get_state()}")
        try:
            self.originator.set_memento(memento)
        except Exception as e:
            self.revert()