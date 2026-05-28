import tkinter
from tkinter import ttk
from tkinter.ttk import Treeview
from typing import Any

from Programms.MDbMonitor.App.Models.Departure import Departure

from Programms.MDbMonitor.Frontend.ViewModels.DepartureTableModel import DepartureTableModel

from Programms.MDbMonitor.lib.DependencyInjector import ServiceCollection

class DepartureTable(tkinter.Frame):

    def __init__(self, parent:tkinter.Widget, services:ServiceCollection):
        super().__init__(parent)
        self.config(background='blue')
        self.data_context:DepartureTableModel = services.get_service(DepartureTableModel)
        columns = ('Departure', 'Late', 'Line', 'Destination', 'Type')
        self.__table:ttk.Treeview = Treeview(self, columns=columns)
        self.__table.column('Departure', width = 80)
        self.__table.heading('Departure', text = 'Departure')
        self.__table.column('Late', width = 120)
        self.__table.heading('Late', text = 'Delay')
        self.__table.column('Line', width = 60)
        self.__table.heading('Line', text = 'Line')
        self.__table.column('Destination', width = 140)
        self.__table.heading('Destination', text = 'Destination')
        self.__table.column('Type', width = 120)
        self.__table.heading('Type', text = 'Type')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__table.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.update_fahrten()

    def update_fahrten(self):
        for item in self.__table.get_children():
            self.__table.delete(item)
        departures:list[Departure] = self.data_context.get_departures()
        for departure in departures:
            self.__table.insert(
                '',
                tkinter.END,
                values=(departure.when.strftime("%H:%M"), f"{ int((departure.delay if departure.delay else 0) / 60) } min", departure.line.name, departure.direction))

