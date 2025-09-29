from typing import override
from .Vogel import Vogel

class Kolibri(Vogel):

    def __init__(self, name:str, alter:int, gewicht:float):
        super().__init__(name, alter, gewicht)

    @override
    def fressen(self):
        print('der dino frisst!')

    @override
    def laut_geben(self):
        print('der dino bellt!')

    @override
    def altern(self):
        print('der dino altert!')
        self.alter-=1