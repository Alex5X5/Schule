import tkinter

from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint

class MainViewModel:

    @DpiEntryPoint
    def __init__(self):
        self.output_text:tkinter.Variable = tkinter.Variable()
        self.input_price_text:tkinter.Variable = tkinter.Variable()
        self.input_volume_text:tkinter.Variable = tkinter.Variable()
        self.input_price_text.trace_add("write", self.input_text_changed)
        self.input_volume_text.trace_add("write", self.input_text_changed)

    def input_text_changed(self, string1: str, string2: str, string3: str):
        try:
            input_price_float=float(self.input_price_text.get())
            input_volume_float=float(self.input_volume_text.get())
            self.output_text.set(str(input_price_float*input_volume_float))
        except ValueError:
            self.output_text.set('invalid input')
