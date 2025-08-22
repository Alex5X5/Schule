import copy
from dataclasses import dataclass

@dataclass
class Inhaber:
    name:str
    id:int

    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id

    def get_id(self) -> int:
        return copy.copy(self.id)

    def __str__(self):
        return f'M21.Inhaber.Inhaber[name={self.name}, id={str(self.id)}]'