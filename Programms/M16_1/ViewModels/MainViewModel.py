import tkinter

class MainViewModel:

    def __init__(self):
        self.entry_text:tkinter.Variable = tkinter.Variable()
        self.entry_text.trace_add("write", self.entry_text_changed)


    def button_1_callback(self):
        print('button 1 was presssed')

    def entry_text_changed(self, string1: str, string2: str, string3: str):
        print(self.entry_text.get())
