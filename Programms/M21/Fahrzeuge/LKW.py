from dataclasses import dataclass

from Programms.M21.Fahrzeuge.Fahrzeug import Fahrzeug


@dataclass
class LKW(Fahrzeug):

    def __init__(self, name:str, hoechstgeschwindigkeit:int, leistung:int, hubraum:int, zylinder:int, gewicht:int):
        super().__init__(name, hoechstgeschwindigkeit, leistung, hubraum, zylinder)
        self.__gewicht = gewicht

    def fahren(self):
        print(f"der LKW fährt lahme {self.Hoechstgeschwindigkeit / 2} kmh!")