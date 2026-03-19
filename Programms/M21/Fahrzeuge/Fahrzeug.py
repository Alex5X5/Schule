from dataclasses import dataclass

@dataclass
class Fahrzeug:

    def __init__(self, name:str, hoechstgeschwindigkeit:int, leistung:int, hubraum:int, zylinder:int):
        self.__name:str = name
        self.__hoechstgeschwindigkeit:int = hoechstgeschwindigkeit
        self.__leistung:int = leistung
        self.__hubraum:int = hubraum
        self.__zylinder:int = zylinder

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, name:str):
        self.__name:str = name

    @property
    def Hoechstgeschwindigkeit(self):
        return self.__hoechstgeschwindigkeit

    @Hoechstgeschwindigkeit.setter
    def Hoechstgeschwindigkeit(self, value:int):
        if value < 1:
            raise ValueError("max Velocity must be greater than 0")
        if value > 300_000:
            raise ValueError("max Velocity must be less than light speed")
        self.__hoechstgeschwindigkeit:int = value

    @property
    def Leistung(self) -> int:
        return self.__leistung

    @Leistung.setter
    def Leistung(self, value:int):
        self.__leistung:int = value

    @property
    def Hubraum(self) -> int:
        return self.__hubraum

    @Hubraum.setter
    def Hubraum(self, value:int):
        if value < 1:
            raise ValueError("Hubraum must be greater than 0")
        self.__hubraum:int = value

    @property
    def Zylinder(self) -> int:
        return self.__zylinder

    @Zylinder.setter
    def Zylinder(self, value:int) -> None:
        if value < 1:
            raise ValueError("Zylinder must be greater than 0")
        self.Zylinder = value

    def fahren(self):
        print('das Fahrzeug fährt!   yupiie!!!!')