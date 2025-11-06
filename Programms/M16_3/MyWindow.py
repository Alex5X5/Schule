import tkinter

from Programms.M16_3.Views.MainView import MainView

class MyWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("Color Selector")
        self.geometry("600x400")

        self.main_view:tkinter.Frame = MainView(self)
        self.main_view.pack(fill="both", expand=True)

        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', False)
