import requests

from Programms.MDbMonitor.Models.Location import Location


class ApiService:

    def __init__(self, base_url:str):
        self.__base_url = base_url
        pass

    def __get_from_api(self, path:str, params:dict[str, str|int]) -> str:
        url = self.__base_url + '/' + path
        response = requests.get(url, params=params)
        return response.json()

    @property
    def locations(self) -> list[Location]:
        params:dict[str, str] = {"query" : "", "results" : 50}
        response:str = self.__get_from_api('locations', params)
        print(response)