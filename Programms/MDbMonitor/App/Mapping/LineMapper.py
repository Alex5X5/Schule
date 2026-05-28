from Programms.MDbMonitor.Api.Models.Line import Line as api_Line
from Programms.MDbMonitor.App.Models.Line import Line
from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint


class LineMapper:

    @DpiEntryPoint
    def __init__(self):
        pass

    def to_domain(self, data:api_Line) -> Line:
        return Line(data.id, data.name)

    def to_api(self, data:Line) -> api_Line:
        return api_Line(data.id, data.name)
