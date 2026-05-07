

class Location:

    def __init__(self, id:int, latitude:int, longitude:int):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Location[id={self.id}, latitude={self.latitude}, longitude={self.longitude}]"