import math
import tkinter

from Programms.M16_3.Main import MainView


class MainWindow(tkinter.Tk):
    """
        Eine Klasse, die alle sichtbaren Elemente innerhalb des Fensters enthält.
    """
    def __init__(self):
        super().__init__()
        self.title("Color Selector")
        self.geometry("600x400")

        #Ingalt hinzufügen
        self.main_view:MainView = MainView(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.main_view.grid(row=0, column=0, sticky="nsew")
        self.main_view.grid(row=0, column=0, sticky="nsew")

        #Fenster in den Fordergrund bringen
        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', False)