from Programms.MDbMonitor.Models.Location import Location


class Station:

    def __init__(self,name:str, id:int, location:Location):
        self.id = id
        self.name = name
        self.location = location

    def __str__(self):
        return f"Station[id={self.id}, name={self.name}, location={self.location}]"