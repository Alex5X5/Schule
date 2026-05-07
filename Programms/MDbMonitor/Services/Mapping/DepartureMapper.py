from datetime import datetime

from Programms.MDbMonitor.Models.Departure import Departure
from Programms.MDbMonitor.Services.DependencyInjector import DpiEntryPoint
from Programms.MDbMonitor.Services.Mapping.LineMapper import LineMapper


class DepartureMapper:

    @DpiEntryPoint
    def __init__(self, line_mapper:LineMapper):
        self.line_mapper = line_mapper

    def to_domain(self, data:dict) -> Departure:
        when = datetime.fromisoformat(data['when'])
        line = self.line_mapper.to_domain(data['line'])
        return Departure(when, data['delay'], line, data['platform'])
