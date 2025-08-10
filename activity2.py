class Animal:
    def move(self):
        pass  # base class method, can be overridden


class Cat(Animal):
    def move(self):
        print("The cat walks silently.")


class Horse(Animal):
    def move(self):
        print("The horse gallops swiftly.")


# Demonstration of polymorphism
animals = [Cat(), Horse()]

for animal in animals:
    animal.move()
