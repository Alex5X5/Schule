from Programms.MDbMonitor.Models.Line import Line
from Programms.MDbMonitor.Services.DependencyInjector import DpiEntryPoint


class LineMapper:

    @DpiEntryPoint
    def __init__(self):
        pass

    def to_domain(self, data:dict) -> Line:
        return Line(data['id'], str(data['name']))
