from Programms.MDbMonitor.Models.Location import Location
from Programms.MDbMonitor.Services.DependencyInjector import DpiEntryPoint


class LocationMapper:

    @DpiEntryPoint
    def __init__(self):
        pass

    def to_domain(self, data:dict) -> Location:
        return Location(data['id'], data['latitude'], data['longitude'])
