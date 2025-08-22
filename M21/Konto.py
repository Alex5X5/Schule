import copy

from  dataclasses import dataclass
from M21.Inhaber import Inhaber


@dataclass
class Konto:
    __inhaber:Inhaber
    __kontonummer:int = 0
    __kontostand:float = 0

    def __init__(self, inhaber:Inhaber, kontonummner:int, kontostand:float):
        self.__inhaber = inhaber
        self.__kontostand = kontostand

    def __str__(self):
        return f'M21.Konto.Konto[inhaber={str(self.__inhaber)}, kontostand={str(self.__kontostand)}, kontonummer={str(self.__kontonummer)}]'

    def get_id(self) -> int:
        return copy.copy(self.__kontonummer)

    def set_kontostand(self, wert:float) -> None:
        self.__kontostand = copy.copy(wert)

    def get_kontostand(self) -> float:
        return copy.copy(self.__kontostand)

    def set_inhaber(self, neuer_inhaber:Inhaber):
        self.__inhaber = neuer_inhaber

    def get_inhaber(self) -> Inhaber:
        return self.__inhaber

    def einzahlen(self, betrag:float):
        self.__kontostand += betrag

    def auszahlen(self, betrag:float):
        self.__kontostand-=betrag

    def ist_ueberzogen(self) -> bool:
        return self.get_kontostand() < 0

    def show(self):
        print(f'der kontostand ist {str(self.__kontostand)}')
