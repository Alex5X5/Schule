from typing import Any
import requests

from Programms.MDbMonitor.Models.Departure import Departure
from Programms.MDbMonitor.Models.Station import Station
from Programms.MDbMonitor.Services.Configuration import Configuration
from Programms.MDbMonitor.Services.DependencyInjector import DpiEntryPoint
from Programms.MDbMonitor.Services.Mapping.StationMapper import StationMapper
from Programms.MDbMonitor.Services.Mapping.DepartureMapper import DepartureMapper
from Programms.MDbMonitor.Services.Mapping.LocationMapper import LocationMapper


class ApiService:

    @DpiEntryPoint
    def __init__(
            self,
            config:Configuration,
            location_mapper:LocationMapper,
            station_mapper:StationMapper,
            departure_mapper:DepartureMapper):
        self.__config:Configuration = config
        self.__location_mapper:LocationMapper = location_mapper
        self.__station_mapper:StationMapper = station_mapper
        self.__departure_mapper:DepartureMapper = departure_mapper

    def __get_from_api(self, path:str, params:dict[str, str|int]) -> list[dict[str, Any]]:
        url = self.__config.base_url + '/' + path
        response = requests.get(url, params=params)
        return response.json()

    def get_stations(self, name:str) -> list[Station]:
        params:dict[str, str] = {"query" : name, "results" : 50}
        result:list[Station] = []
        response:list[dict[str, Any]] = self.__get_from_api('locations', params)
        response = [entry for entry in response if entry.get('type') == 'station']
        for data in response:
            station = self.__station_mapper.to_domain(data)
            result.append(station)
        try:
            pass
        except Exception as e:
            print(f"error getting locations bacause of {e}")
        return result

    def get_departures(self, station:Station) -> list[Departure]:
        params:dict[str, str|int] = {"results" : 50}
        result:list[Departure] = []
        response:Any|None = None
        try:
            response = self.__get_from_api(f'stops/{station.id}/departures', params)
        except Exception as e:
            print(f"error getting departures bacause of {e}")
        if response is None:
            return result
        for data in response['departures']:
            location = self.__departure_mapper.to_domain(data)
            result.append(location)
        return result

