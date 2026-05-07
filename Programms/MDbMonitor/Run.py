from Programms.MDbMonitor.Services.Configuration import Configuration
from Programms.MDbMonitor.Services.ApiService import ApiService
from Programms.MDbMonitor.Services.DependencyInjector import DependencyInjector
from Programms.MDbMonitor.Services.Mapping.DepartureMapper import DepartureMapper
from Programms.MDbMonitor.Services.Mapping.LineMapper import LineMapper
from Programms.MDbMonitor.Services.Mapping.LocationMapper import LocationMapper
from Programms.MDbMonitor.Services.Mapping.StationMapper import StationMapper

builder = DependencyInjector()

builder.register_service_singleton(Configuration)
builder.register_service_singleton(LineMapper)
builder.register_service_singleton(LocationMapper)
builder.register_service_singleton(StationMapper)
builder.register_service_singleton(DepartureMapper)
builder.register_service_singleton(ApiService)

services = builder.build_services()
api = services.get_service(ApiService)

location = api.get_stations("Dresden Neu")[0]
departures = api.get_departures(location)

for departure in departures:
    print(departure.line)

