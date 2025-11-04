import tkinter
from typing import Any

from Programms.M16_1.ViewModels import MainViewModel


class MainView:

    def __init__(self):
        self.window: tkinter.Tk = tkinter.Tk()

        self.DataContext:MainViewModel.MainViewModel = MainViewModel.MainViewModel()

        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_columnconfigure(1, weight=5)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(3, weight=5)
        self.window.grid_columnconfigure(4, weight=3)
        for i in range(5):
            self.window.grid_rowconfigure(0, weight=1)

        self.button1: tkinter.Button = tkinter.Button(self.window, width=10, height=10, command=self.DataContext.button_1_callback)
        self.button1.grid(row=0, column=0, sticky='nsew')
        self.button_close: tkinter.Button = tkinter.Button(self.window, width=10, height=10, bg='red',command=self.window.destroy)
        self.button_close.grid(row=0, column=0, sticky='nsew')
        self.button_close.place(x=100, y=10, width=30, height=30)
        self.entry:tkinter.Entry = tkinter.Entry(self.window, textvariable=self.DataContext.entry_text)
        self.entry.place(x=100, y=100, width=100, height=30)

        self.window.title = "test window"
        self.window.geometry('500x500')

