from Programms.MDbMonitor.Api.Models.Line import Line

class Ride:

    def __init__(self, id:int, line:Line):
        self.id = id
        self.line = line

    def __str__(self):
        return f"Ride[id={self.id}, line={self.line}]"
