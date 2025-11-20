from behavior.iterator.iterator import Iterator


class CollectionImpl:
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.append(item)
    
    def __iter__(self):
        return Iterator(self.items) 