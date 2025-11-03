from .Tier import Tier

class Vogel(Tier):

    def __init__(self, name:str, alter:int, gewicht:float):
        super().__init__(name, alter, gewicht)

