from typing import List
from entity.MountAnimal import MountAnimal


class Camel(MountAnimal):
    bent_quantity: int

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str], bent_quantity: int):
        super().__init__(id, name, date_of_birth, commands)
        self.bent_quantity = bent_quantity

    def to_dict(self) -> dict:
        return {
            "type": "camel",
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "bent_quantity": self.bent_quantity,
            "commands": self.commands
        }

    @classmethod
    def from_json(cls, json_object):
        id = json_object["id"]
        name = json_object["name"]
        date_of_birth = json_object["date_of_birth"]
        commands = json_object["commands"]
        bent_quantity = int(json_object["bent_quantity"])
        return cls(id, name, date_of_birth, commands, bent_quantity)

    def spit(self):
        print("Yackh!")
