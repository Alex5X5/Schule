import copy
from dataclasses import dataclass

@dataclass
class Schueler:
    vorname:str
    nachname:str

    def __init__(self, _vorname:str, _nachnme:str):
        self.vorname = _vorname
        self.nachname = _nachnme

    def get_id(self) -> int:
        return copy.copy(self.id)

    def __str__(self):
        return f'M21.Inhaber.Inhaber[name={self.name}, id={str(self.id)}]'