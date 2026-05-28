

class Location:

    def __init__(self, id:str, latitude:float, longitude:float):
        self.id:str = id
        self.latitude:float = latitude
        self.longitude:float = longitude

    def __str__(self):
        return f"Location[id={self.id}, latitude={self.latitude}, longitude={self.longitude}]"