from Programms.MDbMonitor.Api.Models.Departure import Departure as api_Departure
from Programms.MDbMonitor.App.Models.Departure import Departure
from Programms.MDbMonitor.Api.Models.Station import Station as api_Station
from Programms.MDbMonitor.App.Models.Station import Station
from Programms.MDbMonitor.Api.Models.Location import Location as api_Location

from Programms.MDbMonitor.App.Mapping.StationMapper import StationMapper

from Programms.MDbMonitor.Api.Services.ApiService import ApiService

from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint

class StationService:

    @DpiEntryPoint
    def __init__(self, api:ApiService, mapper:StationMapper):
        self.api = api
        self.mapper = mapper

    def get_station_by_name(self, name:str) -> Station | None:
        stations:list[api_Station] = self.api.get_stations(name)
        if len(stations) < 1:
            return None
        station:api_Station = stations[0]
        return self.mapper.to_api(station)
