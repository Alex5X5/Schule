import tkinter

from Programms.MDbMonitor.App.Services.DepartureService import DepartureService
from Programms.MDbMonitor.App.Services.LineService import LineService
from Programms.MDbMonitor.App.Services.LocationService import LocationService
from Programms.MDbMonitor.App.Services.StationService import StationService
from Programms.MDbMonitor.Frontend.MainWindow import MainWindow
from Programms.MDbMonitor.Shared.Configuration import Configuration
from Programms.MDbMonitor.lib.DependencyInjector import ServiceCollection

from Programms.MDbMonitor.Api.Services.ApiService import ApiService

from Programms.MDbMonitor.App.Mapping.DepartureMapper import DepartureMapper
from Programms.MDbMonitor.App.Mapping.LineMapper import LineMapper
from Programms.MDbMonitor.App.Mapping.LocationMapper import LocationMapper
from Programms.MDbMonitor.App.Mapping.StationMapper import StationMapper

from Programms.MDbMonitor.Frontend.ViewModels.DepartureTableModel import DepartureTableModel
from Programms.MDbMonitor.Frontend.ViewModels.HeaderModel import HeaderModel
from Programms.MDbMonitor.Frontend.ViewModels.MainViewModel import MainViewModel

collection = ServiceCollection()

collection.register_singleton(Configuration)
collection.register_singleton(LineMapper)
collection.register_singleton(LocationMapper)
collection.register_singleton(StationMapper)
collection.register_singleton(DepartureMapper)

collection.register_singleton(ApiService)
collection.register_singleton(LineService)
collection.register_singleton(LocationService)
collection.register_singleton(StationService)
collection.register_singleton(DepartureService)


collection.register_transient(DepartureTableModel)
collection.register_singleton(MainViewModel)
collection.register_transient(HeaderModel)

window:MainWindow = MainWindow(collection)

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