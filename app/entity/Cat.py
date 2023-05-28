from typing import List
from entity.PetAnimal import PetAnimal

class Cat(PetAnimal):
    breed: str

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str], breed: str):
        super().__init__(id, name, date_of_birth, commands)
        self.breed = breed

    def to_dict(self) -> dict:
        return {
            "type": "cat",
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "breed": self.breed,
            "commands": self.commands
        }

    @classmethod
    def from_json(cls, json_object):
        id = json_object["id"]
        name = json_object["name"]
        date_of_birth = json_object["date_of_birth"]
        commands = json_object["commands"]
        breed = json_object["breed"]
        return cls(id, name, date_of_birth, commands, breed)

    def purr(self):
        print("Pur prrrr")
