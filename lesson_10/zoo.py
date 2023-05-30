"""
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.

"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Mammal(Animal):
    def __init__(self, name, age, fur):
        super().__init__(name, age)
        self.fur = fur

    def get_specific(self):
        return self.fur


class Fish(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_specific(self):
        return self.color


class Bird(Animal):
    def __init__(self, name, age, feather):
        super().__init__(name, age)
        self.feather = feather

    def get_specific(self):
        return self.feather


class AnimalFactory:
    def make_animal(self, animal_type, name, age, spec):
        if animal_type == "Mammal":
            return Mammal(name, age, spec)
        elif animal_type == "Bird":
            return Bird(name, age, spec)
        elif animal_type == "Fish":
            return Fish(name, age, spec)
        else:
            raise Exception("What the f..k is this?")


if __name__ == "__main__":
    try:
        factory = AnimalFactory()
        animal = factory.make_animal("Spider", "Shelob", 300, "very angry")
    except Exception as e:
        print(e)
    else:
        print(f'Name: {animal.get_name()}, age: {animal.get_age()}, specs: {animal.get_specific()}')
