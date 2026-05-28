from datetime import datetime

from Programms.MDbMonitor.Api.Models.Line import Line


class Departure:

    def __init__(self, when:str, direction:str,  delay:int, line:Line, plattform:str):
        self.when:str = when
        self.direction:str = direction
        self.delay:int = delay
        self.line:Line = line
        self.platform:str = plattform

    def __str__(self):
        return f"Departure[when={self.when}, delay={self.delay}, line={self.line}, platform={self.platform}]"
