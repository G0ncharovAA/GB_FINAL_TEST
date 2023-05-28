import json
from typing import List, Union
from entity.Dog import Dog
from entity.Cat import Cat
from entity.Horse import Horse
from entity.Hamster import Hamster
from entity.Camel import Camel
from entity.Donkey import Donkey
from entity.PetAnimal import PetAnimal
from entity.MountAnimal import MountAnimal
from Counter import Counter

__filename = "db.json"


def __read():
    with open(__filename, "r") as f:
        animals_json = json.load(f)
        output = []
        for animal in animals_json:
            type = animal["type"]
            if type == "dog":
                output.append(Dog.from_json(animal))
            elif type == "cat":
                output.append(Cat.from_json(animal))
            elif type == "hamster":
                output.append(Hamster.from_json(animal))
            elif type == "horse":
                output.append(Horse.from_json(animal))
            elif type == "camel":
                output.append(Camel.from_json(animal))
            elif type == "donkey":
                output.append(Donkey.from_json(animal))
        return output


def __save(animals: List[Union[Dog, Cat, Hamster, Horse, Camel, Donkey]]):
    a = animals
    animals_dict = [animal.to_dict() for animal in animals]
    with open(__filename, "w") as f:
        json.dump(animals_dict, f)


def read_all():
    return __read()


def add_pet_animal(pet_animal: PetAnimal):
    animals = __read()
    new_id = len(animals)
    pet_animal.id = str(new_id)
    animals.append(pet_animal)
    __save(animals)
    try:
        with Counter() as counter:
            counter.add()
    except Exception as e:
        print(e)


def save_pet_animal(pet_animal: PetAnimal):
    animals = __read()
    filtered_animals = list(filter(lambda animal: animal.id == pet_animal.id, animals))
    index = animals.index(filtered_animals[0])
    animals[index] = pet_animal
    __save(animals)


def add_mount_animal(mount_animal: MountAnimal):
    animals = __read()
    new_id = len(animals)
    mount_animal.id = str(new_id)
    animals.append(mount_animal)
    __save(animals)
    try:
        with Counter() as counter:
            counter.add()
    except Exception as e:
        print(e)


def save_mount_animal(mount_animal: MountAnimal):
    animals = __read()
    filtered_animals = list(filter(lambda animal: animal.id == mount_animal.id, animals))
    index = animals.index(filtered_animals[0])
    animals[index] = mount_animal
    __save(animals)


def get_animal(id: str):
    animals = __read()
    animal = list(filter(lambda animal: animal.id == id, animals))[0]
    return animal
