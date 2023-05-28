from typing import List
from entity.PetAnimal import PetAnimal

class Hamster(PetAnimal):
    furr_color: str

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str], furr_color: str):
        super().__init__(id, name, date_of_birth, commands)
        self.furr_color = furr_color

    def to_dict(self) -> dict:
        return {
            "type": "hamster",
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "furr_color": self.furr_color,
            "commands": self.commands
        }

    @classmethod
    def from_json(cls, json_object):
        id = json_object["id"]
        name = json_object["name"]
        date_of_birth = json_object["date_of_birth"]
        commands = json_object["commands"]
        furr_color = json_object["furr_color"]
        return cls(id, name, date_of_birth, commands, furr_color)

    def scrunch(self):
        print("Gr rrg!")
