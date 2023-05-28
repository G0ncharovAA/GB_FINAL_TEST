from date_store.AnimalsRepository import get_animal, save_pet_animal, save_mount_animal
from entity.MountAnimal import MountAnimal
from entity.PetAnimal import PetAnimal


def select_animal_id():
    print("Введите id животного:")
    return input()


def list_of_animals(animals):
    for animal in animals:
        print(f'id: {animal.id} имя: {animal.name}')


def animal_details(id: str):
    animal = get_animal(id)
    if isinstance(animal, PetAnimal):
        print(animal.to_dict())
        return animal
    elif isinstance(animal, MountAnimal):
        print(animal.to_dict())
        return animal


def add_commands_to_animal(id: str):
    animal = animal_details(id)
    print("Введите название команды для добавления")
    command = input()
    animal.commands.append(command)
    if isinstance(animal, PetAnimal):
        save_pet_animal(animal)
    elif isinstance(animal, MountAnimal):
        save_mount_animal(animal)
