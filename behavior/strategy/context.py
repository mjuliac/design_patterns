from behavior.strategy.strategy import IStrategy

class Context:
    def __init__(self, strategy: IStrategy=None):
        self._strategy = strategy
        
    def set_strategy(self, strategy: IStrategy):
        self._strategy = strategy
        
    def execute_strategy(self):
        self._strategy.execute()