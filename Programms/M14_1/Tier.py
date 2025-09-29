from abc import  ABC, abstractmethod


class Tier(ABC):

    def __init__(self, name:str, alter:int, gewicht:float):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht

    @abstractmethod
    def fressen(self):
        pass

    @abstractmethod
    def laut_geben(self):
        pass

    @abstractmethod
    def altern(self):
        pass