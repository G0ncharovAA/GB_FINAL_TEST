from typing import List
from entity.PetAnimal import PetAnimal


class Dog(PetAnimal):
    mass: float

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str], mass: float):
        super().__init__(id, name, date_of_birth, commands)
        self.mass = mass

    def to_dict(self) -> dict:
        return {
            "type": "dog",
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "mass": self.mass,
            "commands": self.commands
        }

    @classmethod
    def from_json(cls, json_object):
        id = json_object["id"]
        name = json_object["name"]
        date_of_birth = json_object["date_of_birth"]
        commands = json_object["commands"]
        mass = float(json_object["mass"])
        return cls(id, name, date_of_birth, commands, mass)

    def bark(self):
        print("Wow woof!")
