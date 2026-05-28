import tkinter

from Programms.MDbMonitor.Frontend.Components.DepartureTable import DepartureTable
from Programms.MDbMonitor.Frontend.Components.Header import Header
from Programms.MDbMonitor.lib.DependencyInjector import ServiceCollection
from Programms.MDbMonitor.Frontend.ViewModels.MainViewModel import MainViewModel


class MainView(tkinter.Frame):

    def __init__(self, parent:tkinter.Widget, services:ServiceCollection):
        super().__init__(parent)
        self.config(bg="green")
        self.dataContext:MainViewModel = services.get_service(MainViewModel)
        self.table = DepartureTable(self, services)
        self.header = Header(self, services, self.table.data_context.on_update_table, self.table.data_context.on_update_location)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.header.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.table.grid(column=0, row=1, sticky=tkinter.NSEW)
