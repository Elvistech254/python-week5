class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        return "The dog runs on ground"


class Bird(Animal):
    def move(self):
        return "The bird flies in the sky"


class Fish(Animal):
    def move(self):
        return "The fish swims in water"


# Test polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
