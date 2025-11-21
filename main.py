from creationals.singleton import Singleton, MetaclassSingleton, GetInstanceSingleton
from creationals.prototype import Prototype
from creationals.builder.builder import PizzaBuilder
from creationals.builder.director import Director
from creationals.factory.creator import CreatorA, CreatorB
from creationals.abstract_factory.factory import FactoryA, FactoryB

from estructurals.adapter.service import Service
from estructurals.adapter.adapter import Adapter
from estructurals.bridge.abstraction import Abstraction
from estructurals.bridge.concrete import ConcreteImplementationA, ConcreteImplementationB
from estructurals.composite.composite import Composite
from estructurals.composite.item import Item
from estructurals.decorator.component import Component
from estructurals.decorator.decorator import Decorator
from estructurals.facade.facade import Facade
from estructurals.flyweight.flyweight import Flyweight, FlyweightFactory
from estructurals.proxy.proxy import Proxy

from behavior.chain_of_responsibility.handlers import ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC, DefaultHandler
from behavior.command.command import CommandImpl
from behavior.command.invocator import Invocator
from behavior.command.receptor import Receptor
from behavior.interpreter.expresion import Numero, Suma, Resta, Multiplicacion, Division
from behavior.iterator.collection import CollectionImpl
from behavior.mediator.components import ComponentA, ComponentB
from behavior.mediator.mediator import MediatorImpl
from behavior.memento.originator import Originator
from behavior.memento.caregiver import Caregiver

    
class MetaObjSingleton(metaclass=MetaclassSingleton):
    def __init__(self):
        super().__init__()
        self.id = id(self)
        

class ObjBaseSingleton(Singleton):
    def __init__(self):
        super(Singleton).__init__()
        
    def get_id(self):
        return id(self)

    
class ObjectSingleton(GetInstanceSingleton):
    def __init__(self):
        super().__init__()
        self.id = id(self)
     
        
class SingletonClass:
    __instance = None
    
    @staticmethod
    def get_instance():
        if SingletonClass.__instance is None:
            SingletonClass.__instance = SingletonClass()
        return SingletonClass.__instance
    
    def get_id(self):
        return id(self)
    
    def __init__(self):
       if SingletonClass.__instance is not None:
           raise Exception("This class is a singleton!")
       else:
           SingletonClass.__instance = self


class ConcretePrototype(Prototype):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self):
        return f"name:{self.name}, value:{self.value}"

if __name__ == "__main__":
    print("Testing Singleton Implementations:")    
    print("------------------------------") 
    print("Metaclass Singleton:")
    metaObj1 = MetaObjSingleton()   
    metaObj2 = MetaObjSingleton()
    print(metaObj1 is metaObj2)
    print(metaObj1.id, metaObj2.id)
    print("------------------------------") 
    
    
    print("Base Class Singleton:")
    objBase1 = ObjBaseSingleton()   
    objBase2 = ObjBaseSingleton()        
    print(objBase1 is objBase2)
    print(objBase1.get_id(), objBase2.get_id())
    print("------------------------------") 
    
    
    print("Object GetInstanceSingleton:")
    obj1 = ObjectSingleton.get_instance()
    obj2 = ObjectSingleton.get_instance()
    print(obj1 is obj2)
    print(obj1.id, obj2.id)
    print("------------------------------") 
    
    
    print("Singleton Class with Static Method:")
    objClass1 = SingletonClass.get_instance()
    objClass2 = SingletonClass.get_instance()
    print(objClass1 is objClass2) 
    print(objClass1.get_id(), objClass2.get_id()) 
    print("------------------------------")      
    
    
    print("Testing Prototype Implementation:")    
    print("------------------------------")
    prototype1 = ConcretePrototype("Prototype1", [1, 2, 3, {'a': 'A', 'b': 'B'}, [10, 20], (1,2,3)])
    prototype2 = prototype1.clone()
    print(prototype1 is prototype2)
    print(prototype1)
    print(prototype2)
    
    prototype2.value = [4, 5, 6, {'c': 'C', 'd': 'D'}, [30, 40], (4,5,6)]
    print(prototype1 is prototype2)
    print(prototype1)
    print(prototype2)
    print("------------------------------")
    
    
    print("Testing Builder Implementation:")    
    print("------------------------------")
    builder = PizzaBuilder()
    director = Director(builder)
    margarita = director.get_margarita_pizza()
    print("Margarita Pizza:", vars(margarita))
    pepperoni = director.get_pepperoni_pizza()
    print("Pepperoni Pizza:", vars(pepperoni))
    print("------------------------------")
    
    
    print("Testing Factory Implementation:")
    print("------------------------------")
    creator_a = CreatorA()
    product_a = creator_a.create_product()
    print(product_a.descripttion())
    creator_b = CreatorB()
    product_b = creator_b.create_product()
    print(product_b.descripttion())
    print("------------------------------")
    
    
    print("Testing Abstract Factory Implementation:")
    print("------------------------------")
    factory_a = FactoryA()
    product_a1 = factory_a.create_product_a()
    product_b1 = factory_a.create_product_b()
    print(product_a1.descripttion())
    print(product_b1.descripttion())
    factory_b = FactoryB()
    product_a2 = factory_b.create_product_a()
    product_b2 = factory_b.create_product_b()
    print(product_a2.descripttion())
    print(product_b2.descripttion())
    print("------------------------------")
    
    
    print("Testing Adapter Implementation:")
    print("------------------------------")
    service = Service()
    adapter = Adapter(service)
    print(f"The service has {adapter.method1()} and {adapter.method2()}")
    print("------------------------------")


    print("Testing Bridge Implementation:")
    print("------------------------------")
    abstraction_a = Abstraction(ConcreteImplementationA())
    print(abstraction_a.operation())
    abstraction_b = Abstraction(ConcreteImplementationB())
    print(abstraction_b.operation())
    print("------------------------------")
    
    
    print("Testing Composite Implementation:")
    print("------------------------------")
    item1 = Item()
    item2 = Item()
    composite = Composite()
    composite.add(item1)
    composite.add(item2)
    
    item3 = Item()
    composite2 = Composite()
    composite2.add(composite)
    composite2.add(item3)
    composite2.operation()
    print("------------------------------")
    
    
    print("Testing Decorator Implementation:")
    print("------------------------------")
    component = Component()
    decorator = Decorator(component)
    decorator.operation()
    print("------------------------------")
    
    
    print("Testing Facade Implementation:")
    print("------------------------------")
    facade = Facade()
    facade.operation()
    print("------------------------------")
    
    
    print("Testing Flyweight Implementation:")
    print("------------------------------")
    flyweight_factory = FlyweightFactory()
    flyweight1 = flyweight_factory.get_flyweight("A")
    flyweight2 = flyweight_factory.get_flyweight("A")
    flyweight3 = flyweight_factory.get_flyweight("B")
    flyweight1.operation("Unique State 1")
    flyweight2.operation("Unique State 2")
    flyweight3.operation("Unique State 3")
    print(f"Flyweight Factory has {flyweight_factory.get_flyweights_count()} flyweights")
    print("------------------------------")
    
    
    print("Testing Proxy Implementation:")
    print("------------------------------")
    proxy = Proxy()
    proxy.operation()
    print("------------------------------")
    
    
    print("Testing Chain of Responsibility Implementation:")
    print("------------------------------")
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()
    default_handler = DefaultHandler()
    
    handler_a.set_next(handler_b).set_next(handler_c).set_next(default_handler)
    
    for i in [5, 15, 25, 35]:
        handler_a.handle(i)
    
    print("------------------------------")
    
    
    print("Testing Command Implementation:")
    print("------------------------------")
    receptor = Receptor()
    command = CommandImpl(receptor)
    invocator = Invocator(command)
    invocator.execute()
    print("------------------------------")
    
    
    print("Testing Interpreter Implementation:")
    print("------------------------------")
    exp1 = Suma(Numero(10), Numero(20))
    exp2 = Resta(Numero(10), Numero(20))
    exp3 = Multiplicacion(Numero(10), Numero(20))
    exp4 = Division(Numero(10), Numero(20))
    print(exp1.interpret())
    print(exp2.interpret())
    print(exp3.interpret())
    print(exp4.interpret())
    print("------------------------------")
    
    print("Testing Iterator Implementation:")
    print("------------------------------")
    collection = CollectionImpl()
    collection.add("Item 1")
    collection.add("Item 2")
    collection.add("Item 3")
    
    iterator = collection.__iter__()
    while iterator.has_next():
        print(iterator.__next__())
    
    print("")
        
    for item in collection:
        print(item)
    print("------------------------------")
    
    
    print("Testing Mediator Implementation:")
    print("------------------------------")
    mediator = MediatorImpl()
    component_a = ComponentA(mediator)
    component_b = ComponentB(mediator)
    mediator.add_component(component_a)
    mediator.add_component(component_b)
    component_a.send("Hello from Component A")
    component_b.send("Hello from Component B")
    print("------------------------------")
    
    
    print("Testing Memento Implementation:")
    print("------------------------------")
    originator = Originator("1-2-3-4-5.")  
    caregiver = Caregiver(originator)
    caregiver.backup()
    originator.set_state("1-2-3-4.")
    caregiver.backup()
    originator.set_state("1-2-3.")
    caregiver.backup()
    
    originator.set_state("1-2.")
    print(f"Actual State: {originator.state}\n")
    caregiver.revert()
    caregiver.revert()
    caregiver.revert()
    print("------------------------------")
    
    
    
    
    
    