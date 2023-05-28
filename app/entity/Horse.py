from typing import List
from entity.MountAnimal import MountAnimal


class Horse(MountAnimal):
    lear: str

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str], lear: str):
        super().__init__(id, name, date_of_birth, commands)
        self.lear = lear

    def to_dict(self) -> dict:
        return {
            "type": "horse",
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "lear": self.lear,
            "commands": self.commands
        }

    @classmethod
    def from_json(cls, json_object):
        id = json_object["id"]
        name = json_object["name"]
        date_of_birth = json_object["date_of_birth"]
        commands = json_object["commands"]
        lear = json_object["lear"]
        return cls(id, name, date_of_birth, commands, lear)

    def neigh(self):
        print("EEhoho!")
