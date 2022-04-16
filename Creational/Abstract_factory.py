"""
This is an example of Abstract Factory Pattern
"""
from abc import ABC, abstractmethod


class FurnitureFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another
    
    An example of Funirture Factory that can produces chair and sofa 
    """
    
    @abstractmethod
    def create_chair(self):
        pass
    
    @abstractmethod
    def create_sofa(self):
        pass


class ClassicalFurniture(FurnitureFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variants. The factory guarantees that the resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """
    
    def create_chair(self):
        return ClassicalChair()
    
    def create_sofa(self):
        return ClassicalSofa()


class ModernFuniture(FurnitureFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """
    
    def create_chair(self):
        return ModernChair()
    
    def create_sofa(self):
        return ModernSofa()


class Chair(ABC):
    """
    Each distinct product of a product family should have a base interface.
    All variants of the product must implement this interface.
    """
    
    @abstractmethod
    def can_sit(self):
        pass
    
    
"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ClassicalChair(Chair):
    
    def can_sit(self):
        return "You can sit on it from Classical Chair"


class ModernChair(Chair):
    
    def can_sit(self):
        return "You can sit on it from Modern Chair"
    
    
class Sofa(ABC):
    """
    Here's the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    
    @abstractmethod
    def can_sleep(self):
        """
        Product is able to do its own thing
        """
        pass
    
    @abstractmethod
    def can_sit(self, collaborator: Chair):
        """
        But it also can collaborate with the other Product.
        
        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ClassicalSofa(Sofa):
    
    def can_sit(self, collaborator: Chair):
        result = collaborator.can_sit()
        return f"You can sit on it from Classical sofa, with collabortaor ({result})"
    
    def can_sleep(self):
        return "you can sleep from Classical sofa"


class ModernSofa(Sofa):
    
    def can_sit(self, collaborator: Chair):
        result = collaborator.can_sit()
        return f"You can sit on it from Modern sofa, with collaborator ({result})"
    
    def can_sleep(self):
        return "You can sleep from Modern sofa"


def client_code(factory: FurnitureFactory):
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    
    print(f"{sofa.can_sleep()}")
    print(f"{sofa.can_sit(chair)}")
    

if __name__ == '__main__':
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type")
    client_code(ClassicalFurniture())
    
    print("\n")
    
    print("Client: Testing the same client code with the second factory type")
    client_code(ModernFuniture())
    