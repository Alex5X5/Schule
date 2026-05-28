from Programms.MDbMonitor.Api.Models.Station import Station as api_Station
from Programms.MDbMonitor.App.Models.Station import Station
from Programms.MDbMonitor.App.Mapping.LocationMapper import LocationMapper
from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint


class StationMapper:

    @DpiEntryPoint
    def __init__(self, location_mapper:LocationMapper):
        self.__location_mapper = location_mapper

    def to_domain(self, data:api_Station) -> Station:
        location = self.__location_mapper.to_domain(data.location)
        return Station(data.name, data.id, location)

    def to_api(self, data:Station) -> api_Station:
        location = self.__location_mapper.to_api(data.location)
        return api_Station(data.name, data.id, location)
