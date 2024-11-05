#polymorphism
class Cat:
    def __init__(self):
        pass

    def make_sound(self):
        return "A cat purrs"

class Dog:
    def __init__(self):
        pass

    def make_sound(self):
        return "A dog barks"

animal1 = Cat()
print(animal1.make_sound())
animal2 = Dog()
print(animal2.make_sound())