from dataclasses import dataclass
from typing import override

from Programms.M21.Fahrzeuge.Fahrzeug import Fahrzeug


@dataclass
class Auto(Fahrzeug):

    def __init__(self, name:str, hoechstgeschwindigkeit:int, leistung:int, hubraum:int, zylinder:int, laenge:float):
        super().__init__(name, hoechstgeschwindigkeit, leistung, hubraum, zylinder)
        self.__laenge:float = laenge

    @override
    def fahren(self):
        print(f"das Auto fährt mit {self.Hoechstgeschwindigkeit} kmh!")

    @property
    def Laenge(self):
        return self.__laenge

    @Laenge.setter
    def laenge(self, laenge:int):
        self.__laenge = laenge