import tkinter

from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint, ServiceCollection

from Programms.MDbMonitor.App.Services.DepartureService import DepartureService
from Programms.MDbMonitor.App.Services.StationService import StationService

from Programms.MDbMonitor.App.Models.Departure import Departure

class DepartureTableModel:

    @DpiEntryPoint
    def __init__(self, services:ServiceCollection):
        self.departure_service:DepartureService = services.get_service(DepartureService)
        self.station_service:StationService = services.get_service(StationService)
        self.station_name:str = "Dresden"

    def get_departures(self) -> list[Departure]:
        station = self.station_service.get_station_by_name(self.station_name)
        return self.departure_service.get_all_departures(station)

    def on_update_table(self):
        pass

    def on_update_location(self):
        pass
