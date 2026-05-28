from Programms.MDbMonitor.Api.Models.Departure import Departure as api_Departure
from Programms.MDbMonitor.App.Models.Departure import Departure
from Programms.MDbMonitor.Api.Models.Station import Station as api_Station
from Programms.MDbMonitor.App.Models.Station import Station
from Programms.MDbMonitor.Api.Models.Location import Location as api_Location

from Programms.MDbMonitor.App.Mapping.DepartureMapper import DepartureMapper
from Programms.MDbMonitor.App.Mapping.StationMapper import StationMapper

from Programms.MDbMonitor.Api.Services.ApiService import ApiService

from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint

class DepartureService:

    @DpiEntryPoint
    def __init__(self, api:ApiService, mapper:DepartureMapper, station_mapper:StationMapper):
        self.api:ApiService = api
        self.departure_mapper:DepartureMapper = mapper
        self.station_mapper:StationMapper = station_mapper

    def get_all_departures(self, station:Station) -> list[Departure]:
        departures:list[api_Departure] = self.api.get_departures(self.station_mapper.to_api(station))
        return [self.departure_mapper.to_domain(departure) for departure in departures]
