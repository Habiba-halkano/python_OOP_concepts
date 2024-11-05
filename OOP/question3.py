#inheritance
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        return f"An animal sleeps"


class Dog(Animal):
    def __init__(self):
     super().__init__()

    def eat(self):
        return f"A dog eats" #method overriding

    def bark(self):
        return f"A dog barks"


animal1 = Dog()
print(animal1.sleep())
print(animal1.eat())
print(animal1.bark())