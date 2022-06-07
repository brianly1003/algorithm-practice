class Cat:
    pass

class Dog:
    # Class Attributes
    species = "mammal"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says '{}'".format(self.name, sound)

class Poodle(Dog):
    def run(self, speed):
        return "{} run {}".format(self.name, speed)

if __name__ == "__main__":
    cat = Cat()

    minMin = Dog("MinMin", 2)

    print(minMin.description())
    print(minMin.speak("Baba"))

    minMin = Poodle("MinMin1", 3)
    print(minMin.run(30))



