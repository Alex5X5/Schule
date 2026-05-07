from Programms.MDbMonitor.Models.Station import Station
from Programms.MDbMonitor.Services.DependencyInjector import DpiEntryPoint
from Programms.MDbMonitor.Services.Mapping.LocationMapper import LocationMapper


class StationMapper:

    @DpiEntryPoint
    def __init__(self, location_mapper:LocationMapper):
        self.__location_mapper = location_mapper

    def to_domain(self, data:dict) -> Station:
        location = self.__location_mapper.to_domain(data['location'])
        return Station(data['name'], data['id'], location)
