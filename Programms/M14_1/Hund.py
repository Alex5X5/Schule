from typing import override

from .Säugetier import Säugetier

class Hund(Säugetier):

    def __init__(self, name:str, alter:int, gewicht:float):
        super().__init__(name, alter, gewicht)

    @override
    def fressen(self):
        print('der hund frisst!')

    @override
    def laut_geben(self):
        print('der hund bellt!')

    @override
    def altern(self):
        print('der hund altert!')
        self.alter-=1