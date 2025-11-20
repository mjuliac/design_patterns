from creationals.builder.product import Pizza

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
        
    def set_size(self, size):
        self.pizza.size = size
    
    def add_cheese(self):
        self.pizza.cheese = True
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
    
    def add_bacon(self):
        self.pizza.bacon = True
    
    def add_ham(self):
        self.pizza.ham = True
    
    def add_mushrooms(self):
        self.pizza.mushrooms = True
    
    def add_onions(self):
        self.pizza.onions = True
    
    def add_peppers(self):
        self.pizza.peppers = True
        
    def add_olives(self):
        self.pizza.olives = True
        
    def add_tomatoes(self):
        self.pizza.tomatoes = True
        
    def set_massa_type(self, massa_type):
        self.pizza.massa_type = massa_type
        
    def get_pizza(self):
        return self.pizza