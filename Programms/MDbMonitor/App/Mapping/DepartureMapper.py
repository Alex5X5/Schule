from datetime import datetime

from Programms.MDbMonitor.App.Models.Departure import Departure
from Programms.MDbMonitor.Api.Models.Departure import Departure as api_Departure

from Programms.MDbMonitor.App.Mapping.LineMapper import LineMapper

from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint


class DepartureMapper:

    @DpiEntryPoint
    def __init__(self, line_mapper:LineMapper):
        self.line_mapper = line_mapper

    def to_domain(self, data:api_Departure) -> Departure|None:
        try:
            when = datetime.fromisoformat(data.when)
            line = self.line_mapper.to_domain(data.line)
            return Departure(when, data.direction, data.delay, line, data.platform)
        except TypeError as e:
            print(f'failed to convert to domain because of {e}')
        return None
