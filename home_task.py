# 1. Создайте базовый класс `Animal`,
# который будет содержать общие атрибуты
# (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# # 3. Продемонстрируйте полиморфизм: создайте функцию
# `animal_sound(animals)`, которая принимает список животных и вызывает
# метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет
# содержать информацию о животных и сотрудниках. Должны быть методы
# для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`,
# `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).
#

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает")

class Bird(Animal):
    def make_sound(self):
        print("Чирик")

class Mammal(Animal):
    def make_sound(self):
        print("лает гав")

class Reptile(Animal):
    def make_sound(self):
        print("шипение")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.stuff = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name}  добавлено в зоопарк")
    def add_stuff(self, new_stuff):
        self.animals.append(new_stuff)
        print(f"Сотрудник  {new_stuff.name} добавлен в зоопарк")

class Zookeeper():
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):
        print(f"Сотрудник {self.name} кормит {animal.name}")

class Veterinarian():
    def __init__(self, name):
        self.name = name
    def heel_animal(self, animal):
        print(f"Ветеринар {self.name} лечит {animal.name}")

bird1 = Bird("Орел", 3)
mammal1 = Mammal("Жучка", 2)
reptile1 = Reptile("Питон", 4)

zoo = Zoo()
keeper1 = Zookeeper("Вася")
veterinarian1 = Veterinarian("Степа")

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_stuff(keeper1)
zoo.add_stuff(veterinarian1)

# for animal in [bird1, mammal1, reptile1]:
#     print(animal.name, animal.age)
#     animal.make_sound()


keeper1.feed_animal(bird1)
veterinarian1.heel_animal(reptile1)

animal_sound(zoo.animals)