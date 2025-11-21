class Caregiver:
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []
        
    def backup(self):
        print("Caretaker: Saving Originator's state...")
        self._mementos.append(self._originator.create_memento())
        
    def revert(self):
        if not self._mementos:
            return
        
        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_state()}")
        try:
            self._originator.set_memento(memento)
        except Exception as e:
            self.undo()
            
    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_state())