class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        pass

    def sleep(self):
        pass

class Bird(Animal):
    def fly(self):
        pass

class Fish(Animal):
    def swim(self):
        pass

class Mammal(Animal):
    def walk(self):
        pass

if __name__ == "__main__":
    bird = Bird("Голубь", 2)
    fish = Fish("Карась", 1)
    mammal = Mammal("Лев", 5)

    print(f"{bird.name}, возраст: {bird.age}")
    bird.eat()
    bird.fly()

    print(f"{fish.name}, возраст: {fish.age}")
    fish.sleep()
    fish.swim()

    print(f"{mammal.name}, возраст: {mammal.age}")
    mammal.eat()
    mammal.walk()
