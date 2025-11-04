import tkinter
from typing import Any

from Programms.M16_1.ViewModels import MainViewModel


class MainView(tkinter.Frame):

    def __init__(self):
        super().__init__()
        self.window: tkinter.Tk = tkinter.Tk()

        self.DataContext:MainViewModel.MainViewModel = MainViewModel.MainViewModel()

        self.window.grid_columnconfigure(0, weight=6)
        self.window.grid_columnconfigure(1, weight=10)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(3, weight=10)
        self.window.grid_columnconfigure(4, weight=4)
        self.window.grid_columnconfigure(5, weight=2)

        self.window.grid_rowconfigure(0, weight=1)
        for i in range(1,6):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_rowconfigure(6, weight=1)
        self.button1: tkinter.Button = tkinter.Button(self.window, command=self.DataContext.button_1_callback)
        self.button1.grid(row=0, column=0, sticky='nsew')
        self.button_close: tkinter.Button = tkinter.Button(self.window, bg='red',command=self.window.destroy)
        self.button_close.grid(row=0, column=5, sticky='nsew')
        self.input_volume_decription_label:tkinter.Label = tkinter.Label(self.window, text="Volumen in Liter")
        self.input_volume_decription_label.grid(row=1, column=1, sticky='nsew')
        self.input_price_decription_label:tkinter.Label = tkinter.Label(self.window, text="Preis in Euro pro Liter")
        self.input_price_decription_label.grid(row=3, column=1, sticky='nsew')
        self.input_price_entry:tkinter.Entry = tkinter.Entry(self.window, textvariable=self.DataContext.input_price_text)
        self.input_price_entry.grid(row=1, column=3, sticky='nsew')
        self.input_volume_entry:tkinter.Entry = tkinter.Entry(self.window, textvariable=self.DataContext.input_volume_text)
        self.input_volume_entry.grid(row=3, column=3, sticky='nsew')
        self.output_entry:tkinter.Entry = tkinter.Entry(self.window, textvariable=self.DataContext.output_text)
        self.output_entry.grid(row=5, column=3, sticky='nsew')

        self.window.title = "test window"
        self.window.geometry('500x500')

