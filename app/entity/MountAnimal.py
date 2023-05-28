from abc import abstractmethod
from typing import List


class MountAnimal:
    id: str
    name: str
    date_of_birth: str
    commands: List[str]

    def __init__(self, id: str, name: str, date_of_birth: str, commands: List[str]):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.commands = commands

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_json(cls, json_object):
        pass

    def add_command(self, command: str):
        self.commands.append(command)
