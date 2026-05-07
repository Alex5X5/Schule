from datetime import datetime

from charset_normalizer.api import explain_handler

from Programms.MDbMonitor.Models.Line import Line


class Departure:

    def __init__(self, when:datetime, delay:int, line:Line, plattform:str):
        self.when = when
        self.delay = delay
        self.line = line
        self.plattform = plattform

    def __str__(self):
        return f"Departure[when={self.when}, delay={self.delay}, line={self.line}, platform={self.plattform}]"
