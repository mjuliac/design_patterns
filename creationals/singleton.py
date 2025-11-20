class MetaclassSingleton(type):
    """
    A metaclass for Singleton pattern implementation.
    Ensures that only one instance of a class is created.
    """
    _creates = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._creates:
            cls._creates[cls] = super(MetaclassSingleton, cls).__call__(*args, **kwargs)

        return cls._creates[cls]
          
class Singleton:
    """
    A base class for Singleton pattern implementation.
    Ensures that only one instance of a class is created.
    """
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


class GetInstanceSingleton:
    """
    A base class for Singleton pattern implementation.
    Ensures that only one instance of a class is created.
    """
    __instances = {}
        
    @classmethod
    def get_instance(cls):
        if cls not in cls.__instances:
            cls.__instances[cls] = cls()
        return cls.__instances[cls]
        
    def __init__(self):
        pass