from typing import List
from entity.MountAnimal import MountAnimal


class Donkey(MountAnimal):
    capacity: float

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str], capacity: float):
        super().__init__(id, name, date_of_birth, commands)
        self.capacity = capacity

    def to_dict(self) -> dict:
        return {
            "type": "donkey",
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "capacity": self.capacity,
            "commands": self.commands
        }

    @classmethod
    def from_json(cls, json_object):
        id = json_object["id"]
        name = json_object["name"]
        date_of_birth = json_object["date_of_birth"]
        commands = json_object["commands"]
        capacity = float(json_object["capacity"])
        return cls(id, name, date_of_birth, commands, capacity)

    def kick(self):
        print("Hurts alot!")
