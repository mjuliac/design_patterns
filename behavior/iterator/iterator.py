class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.collection)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration