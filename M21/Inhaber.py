from dataclasses import dataclass

@dataclass
class Inhaber:
    name:str
    id:int

    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
