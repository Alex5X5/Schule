from  dataclasses import dataclass

from M21.Inhaber import Inhaber


@dataclass
class Konto:
    inhaber_:Inhaber
    kontonummer:int = 0

    def __init__(self, inhaber:Inhaber):
        self.inhaber_ = inhaber

