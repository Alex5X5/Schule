from datetime import datetime
from typing import Any
import requests

from Programms.MDbMonitor.Api.Models.Departure import Departure
from Programms.MDbMonitor.Api.Models.Line import Line
from Programms.MDbMonitor.Api.Models.Location import Location
from Programms.MDbMonitor.Api.Models.Station import Station
from Programms.MDbMonitor.Shared.Configuration import Configuration
from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint


class ApiService:

    @DpiEntryPoint
    def __init__(
            self,
            config:Configuration):
        self.__config:Configuration = config

    def __get_from_api(self, path:str, params:dict[str, str|int]) -> list[dict[str, Any]]:
        url = self.__config.base_url + '/' + path
        return {'departures':[]}
#        response = requests.get(url, params=params)
#        return response.json()

    def get_locations(self) -> Station:
        return None

    def get_stations(self, name:str) -> list[Station]:
        params:dict[str, str] = {"query" : name, "results" : 50}
        result:list[Station] = []
        response:list[dict[str, Any]] = self.__get_from_api('locations', params)
        response = [entry for entry in response if isinstance(entry, dict) and entry.get('type') == 'station']
        for data in response:
            location = Location(data['location']['id'], data['location']['latitude'], data['location']['longitude'])
            station = Station(data['name'], data['id'], location)
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
            print(f"error getting departures because of {e}")
        if response is None:
            return result
        for data in response['departures']:
            line = Line(data['line']['id'], str(data['line']['name']))
            departure = Departure(data['when'], data['direction'], data['delay'], line, data['platform'])
            result.append(departure)
        return result

