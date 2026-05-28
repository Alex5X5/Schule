from Programms.MDbMonitor.Api.Models.Location import Location as api_Location
from Programms.MDbMonitor.App.Models.Location import Location
from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint


class LocationMapper:

    @DpiEntryPoint
    def __init__(self):
        pass

    def to_domain(self, data:api_Location) -> Location:
        return Location(data.id, data.latitude, data.longitude)

    def to_api(self, data:Location) -> api_Location:
        return api_Location(data.id, data.latitude, data.longitude)
