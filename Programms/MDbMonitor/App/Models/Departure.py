from datetime import datetime

from Programms.MDbMonitor.App.Models.Line import Line


class Departure:

    def __init__(self, when:datetime, direction:str, delay:int, line:Line, platform:str):
        self.when:datetime = when
        self.direction:str = direction
        self.delay = delay
        self.line = line
        self.platform:str = platform

    def __str__(self):
        return f"Departure[when={self.when}, delay={self.delay}, line={self.line}, platform={self.platform}]"
