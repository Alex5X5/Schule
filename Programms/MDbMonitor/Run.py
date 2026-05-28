import tkinter

from Programms.MDbMonitor.App.Services.DepartureService import DepartureService
from Programms.MDbMonitor.App.Services.LineService import LineService
from Programms.MDbMonitor.App.Services.LocationService import LocationService
from Programms.MDbMonitor.App.Services.StationService import StationService
from Programms.MDbMonitor.Frontend.MainWindow import MainWindow
from Programms.MDbMonitor.Frontend.ViewModels.HeaderModel import HeaderModel
from Programms.MDbMonitor.Frontend.Views.MainView import MainView
from Programms.MDbMonitor.Shared.Configuration import Configuration
from Programms.MDbMonitor.lib.DependencyInjector import DependencyInjector

from Programms.MDbMonitor.Api.Services.ApiService import ApiService

from Programms.MDbMonitor.App.Mapping.DepartureMapper import DepartureMapper
from Programms.MDbMonitor.App.Mapping.LineMapper import LineMapper
from Programms.MDbMonitor.App.Mapping.LocationMapper import LocationMapper
from Programms.MDbMonitor.App.Mapping.StationMapper import StationMapper

from Programms.MDbMonitor.Frontend.ViewModels.DepartureTableModel import DepartureTableModel

builder = DependencyInjector()

builder.register_service_singleton(Configuration)
builder.register_service_singleton(LineMapper)
builder.register_service_singleton(LocationMapper)
builder.register_service_singleton(StationMapper)
builder.register_service_singleton(DepartureMapper)

builder.register_service_singleton(ApiService)
builder.register_service_singleton(LineService)
builder.register_service_singleton(LocationService)
builder.register_service_singleton(StationService)
builder.register_service_singleton(DepartureService)


builder.register_service_singleton(DepartureTableModel)
builder.register_service_singleton(HeaderModel)

services = builder.build_services()

window:MainWindow = MainWindow(services)

#window.main_view = MainView(window, services)

#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)
#window.main_view.grid(column=0, row=0, sticky=tkinter.NSEW)
#api = services.get_service(ApiService)

#location = api.get_stations("Dresden Neu")[0]
#departures = api.get_departures(location)

#for departure in departures:
#    print(departure.line)

window.mainloop()