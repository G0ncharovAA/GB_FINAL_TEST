from date_store.AnimalsRepository import add_pet_animal, add_mount_animal
from entity.Dog import Dog
from entity.Cat import Cat
from entity.Horse import Horse
from entity.Hamster import Hamster
from entity.Camel import Camel
from entity.Donkey import Donkey


def add_animal_menu():
    print("Выберите тип животного:")
    print("1 - Домашние животные")
    print("2 - Вьючные животные")
    animal_type = input()
    if animal_type == "1":
        add_new_pet_animal()
    elif animal_type == "2":
        add_new_mount_animal()


def add_new_pet_animal():
    print("Выберите класс животного:")
    print("1 - Собаки")
    print("2 - Кошки")
    print("3 - Хомяки")
    animal_class = input()
    if animal_class == "1":
        add_dog()
    elif animal_class == "2":
        add_cat()
    elif animal_class == "3":
        add_hamster()


def add_new_mount_animal():
    print("Выберите класс животного:")
    print("1 - Лошади")
    print("2 - Верблюды")
    print("3 - Ослы")
    animal_class = input()
    if animal_class == "1":
        add_horse()
    elif animal_class == "2":
        add_camel()
    elif animal_class == "3":
        add_donkey()


def add_dog():
    print("Выберите имя собаки:")
    name = input()
    print("Введите дату рождения собаки:")
    date_of_birth = input()
    print("Введите массу собаки:")
    mass = float(input())
    dog = Dog(id="-1", name=name, date_of_birth=date_of_birth, mass=mass, commands=[])
    add_pet_animal(dog)


def add_cat():
    print("Выберите имя кошки:")
    name = input()
    print("Введите дату рождения кошки:")
    date_of_birth = input()
    print("Введите породу кошки:")
    breed = input()
    cat = Cat(id="-1", name=name, date_of_birth=date_of_birth, breed=breed, commands=[])
    add_pet_animal(cat)


def add_hamster():
    print("Выберите имя хомяка:")
    name = input()
    print("Введите дату рождения хомяка:")
    date_of_birth = input()
    print("Введите цвет шерсти хомяка:")
    furr_color = input()
    hamster = Hamster(id="-1", name=name, date_of_birth=date_of_birth, furr_color=furr_color, commands=[])
    add_pet_animal(hamster)


def add_horse():
    print("Выберите имя лошади:")
    name = input()
    print("Введите дату рождения лошади:")
    date_of_birth = input()
    print("Введите масть лошади:")
    lear = input()
    horse = Horse(id="-1", name=name, date_of_birth=date_of_birth, lear=lear, commands=[])
    add_mount_animal(horse)


def add_camel():
    print("Выберите имя верблюда:")
    name = input()
    print("Введите дату рождения верблюда:")
    date_of_birth = input()
    print("Введите количество горбов верблюда:")
    bent_quantity = int(input())
    camel = Camel(id="-1", name=name, date_of_birth=date_of_birth, bent_quantity=bent_quantity, commands=[])
    add_mount_animal(camel)


def add_donkey():
    print("Выберите имя осла:")
    name = input()
    print("Введите дату рождения осла:")
    date_of_birth = input()
    print("Введите грузоподъемность осла:")
    capacity = float(input())
    donkey = Donkey(id="-1", name=name, date_of_birth=date_of_birth, capacity=capacity, commands=[])
    add_mount_animal(donkey)
