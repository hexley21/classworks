class Animal:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def info(self):
        print(f"Name: {self._name}\nAge: {self._age}")

class Dog(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age)
        self.__breed = breed
        self.__color = color

    def info(self):
        super().info()
        print(f"Breed: {self.__breed}\nColor: {self.__color}")

default_animal = Animal("Animal", 1)
hachiko = Dog("Hachiko", 12, "Akita Inu", "white")

default_animal.info(); print()
hachiko.info()