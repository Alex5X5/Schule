import tkinter

from Programms.MDbMonitor.Frontend.Views.MainView import MainView
from Programms.MDbMonitor.lib.DependencyInjector import ServiceCollection


class MainWindow(tkinter.Tk):

    def __init__(self, services:ServiceCollection):
        super().__init__()
        self.title("Verbindungs Dings")
        self.geometry("600x400")

        self.main_view:tkinter.Frame = MainView(self, services)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.main_view.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', False)
