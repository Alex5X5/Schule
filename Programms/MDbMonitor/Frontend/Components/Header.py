import tkinter
from typing import Any, Callable

from ttkwidgets.autocomplete import AutocompleteCombobox

from Programms.MDbMonitor.Frontend.ViewModels.HeaderModel import HeaderModel

from Programms.MDbMonitor.lib.DependencyInjector import ServiceCollection

class Header(tkinter.Frame):

    def __init__(self, parent:tkinter.Widget, services:ServiceCollection, on_refresh_table:Callable[[], None], on_refresh_location:Callable[[str], None]):
        super().__init__(parent)
        self.data_context:Any = services.get_service(HeaderModel)

        def refresh_table_callback():
            on_refresh_table()

        def refresh_location_callback(arg):
            text = self.__location_combo_box.get().strip()
            if len(text) > 2:
                on_refresh_location(text)

        self.__refresh_button:tkinter.Button = tkinter.Button(self, command=refresh_table_callback)
        self.__location_combo_box:AutocompleteCombobox = AutocompleteCombobox(self, width=30)
        self.__location_combo_box.bind("<KeyRelease>", refresh_location_callback)

        self.config(background='brown')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=3)
        self.grid_columnconfigure(6, weight=1)

        self.__refresh_button.grid(row=1, column=3, sticky=tkinter.NSEW)
        self.__location_combo_box.grid(row=1, column=5, sticky=tkinter.NSEW)