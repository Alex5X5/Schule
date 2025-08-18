from dataclasses import dataclass

@dataclass
class Inhaber:
    name_:str

    def __init__(self, name:str):
        self.name_ = name
