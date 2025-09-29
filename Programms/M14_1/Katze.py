from typing import override

from .Säugetier import Säugetier

class Katze(Säugetier):

    def __init__(self, name:str, alter:int, gewicht:float):
        super().__init__(name, alter, gewicht)

    @override
    def fressen(self):
        print('die Katze frisst!')

    @override
    def laut_geben(self):
        print('die Katze bellt!')

    @override
    def altern(self):
        print('die Katze altert!')
        self.alter-=1