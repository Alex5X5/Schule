from dataclasses import dataclass

@dataclass
class Gleis:
    nummer:int

@dataclass
class Linie:
    nummer:int

@dataclass
class Bahnhof:
    name:str
    gleise:list[Gleis]

@dataclass
class Abfahrt:
    nummer:Linie
    gleis:int

@dataclass
class Ankunft:
    nummer:Linie
    gleis:int

@dataclass
class Fahrt:
    pass
    start:Bahnhof
    ziel:Bahnhof
    abfahrten:list[Abfahrt|None]
    ankunfte:list[Ankunft|None]




test = "5"
print(4 + int(test))