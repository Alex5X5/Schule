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

    def einzahlen(self, betrag:float):
        self.__kontostand += betrag

    def auszahlen(self, betrag:float):
        self.__kontostand-=betrag

    def show(self):
        print(str(self.__kontostand))
