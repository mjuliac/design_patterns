class Director:
    def __init__(self, builder):
        self._builder = builder

    def get_margarita_pizza(self):
        self._builder.set_size("12 inches")
        self._builder.add_cheese()
        self._builder.add_tomatoes()
        self._builder.set_massa_type("Thin Crust")
        return self._builder.get_pizza()
    
    def get_pepperoni_pizza(self):
        self._builder.set_size("14 inches")
        self._builder.add_cheese()
        self._builder.add_pepperoni()
        self._builder.add_onions()
        self._builder.set_massa_type("Thick Crust")
        return self._builder.get_pizza()
   