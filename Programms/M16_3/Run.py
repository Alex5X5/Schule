import math
import tkinter


class MainWindow(tkinter.Tk):
    """
        Eine Klasse, die alle sichtbaren Elemente innerhalb des Fensters enthält.
    """
    def __init__(self):
        super().__init__()
        self.title("Color Selector")
        self.geometry("600x400")

        #Ingalt hinzufügen
        self.main_view:tkinter.Frame = MainView(self)
        self.main_view.pack(fill="both", expand=True)

        #Fenster in den Fordergrund bringen
        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', False)



class MainView(tkinter.Frame):
    """
        Eine Klasse, die alle sichtbaren Elemente innerhalb des Fensters enthält.
    """

    def __init__(self, master:tkinter.Misc):
        """
            Hier werden alle widgets initialisiert und anschließend angeordnet.
        """
        super().__init__(master, bg='white')

        self.view_model:MainViewModel = MainViewModel()

        #alle frames instanziieren
        self.main_frame:tkinter.Frame = tkinter.Frame(self, bg='white')
        self.sliders_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')
        self.labels_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')
        self.rectangles_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')
        self.mixed_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')

        #alle slider instanziieren
        self.slider_red:tkinter.Scale = tkinter.Scale(
            self.sliders_frame,
            from_=0,
            to=255,
            variable=self.view_model.value_red,
            orient=tkinter.HORIZONTAL,
            length=50)
        self.slider_green:tkinter.Scale = tkinter.Scale(
            self.sliders_frame,
            from_=0,
            to=255,
            variable=self.view_model.value_green,
            orient=tkinter.HORIZONTAL,
            length=50)
        self.slider_blue:tkinter.Scale = tkinter.Scale(
            self.sliders_frame,
            from_=0,
            to=255,
            variable=self.view_model.value_blue,
            orient=tkinter.HORIZONTAL,
            length=50)

        #alle labels instanziieren
        self.label_red:tkinter.Label = tkinter.Label(self.labels_frame, text='red', bg='white')
        self.label_green:tkinter.Label = tkinter.Label(self.labels_frame, text='green', bg='white')
        self.label_blue:tkinter.Label = tkinter.Label(self.labels_frame, text='blue', bg='white')

        #alle farbigen Rechtecke instanziieren
        self.rectangle_red:tkinter.Frame = tkinter.Frame(self.rectangles_frame, bg='red')
        self.rectangle_green:tkinter.Frame = tkinter.Frame(self.rectangles_frame, bg='green')
        self.rectangle_blue:tkinter.Frame = tkinter.Frame(self.rectangles_frame, bg='blue')
        self.rectangle_mixed:tkinter.Frame = tkinter.Frame(self.mixed_frame)

        #die on_color_changed methode an die changed events der Farbwerte binden
        self.view_model.value_red.trace_add('write', self.on_color_changed)
        self.view_model.value_green.trace_add('write', self.on_color_changed)
        self.view_model.value_blue.trace_add('write', self.on_color_changed)

        #die grids setzen
        self.grid_configure_components()
        self.grid_components()

        #die Farbwerte auf einen Anfangswert setzen
        self.view_model.value_red.set(0)
        self.view_model.value_green.set(0)
        self.view_model.value_blue.set(0)


    def grid_configure_components(self):
        """
            Konfiguriert die grid layouts aller frames im fenster.
        """
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=20)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_columnconfigure(2, weight=1)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=5)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=2)
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=2)

        #da der slider frame, der labels frame, der rectangles_frame und der mixed_frame das gleiche
        # grid layout haben, kann deren grid layout in einer Schleife durchgeführt werden.
        for component in [self.sliders_frame, self.labels_frame, self.rectangles_frame, self.mixed_frame]:
            for i in range(7):
                component.grid_rowconfigure(i, weight=5 if i%2==0 else 1)
            component.grid_columnconfigure(0, weight=1)
            component.grid_columnconfigure(1, weight=10)
            component.grid_columnconfigure(2, weight=1)


    def grid_components(self):
        """
            Gridet alle elemente des gui.
        """
        self.main_frame.grid(row=1, column=1, sticky='nsew')

        self.sliders_frame.grid(row=0, column=0, sticky='nswe')
        self.labels_frame.grid(row=0, column=1, sticky='nsew')
        self.rectangles_frame.grid(row=0, column=2, sticky='nsew')
        self.mixed_frame.grid(row=0, column=4, sticky='nsew')

        self.slider_red.grid(row=1, column=1, sticky='nsew')
        self.slider_green.grid(row=3, column=1, sticky='nsew')
        self.slider_blue.grid(row=5, column=1, sticky='nsew')

        self.label_red.grid(row=1, column=1, sticky='nsew')
        self.label_green.grid(row=3, column=1, sticky='nsew')
        self.label_blue.grid(row=5, column=1, sticky='nsew')

        self.rectangle_red.grid(row=1, column=1, sticky='nsew')
        self.rectangle_green.grid(row=3, column=1, sticky='nsew')
        self.rectangle_blue.grid(row=5, column=1, sticky='nsew')

        self.rectangle_mixed.grid(row=1, rowspan=5,  column=1, sticky='nsew')


    def on_color_changed(self, s1:str, s2:str, s3:str):
        """
            Verwandelt die drei farbwerte in einen string mit den Hexadezimalzahlen der Farbwerte und setz diesen
            als die farbe des mixed_rectangle.
            Wird aufgerufen, falls sich ein Farbwert des view_model ändert.
        """
        self.rectangle_mixed.configure(bg=self.view_model.get_mixed_color())



class MainViewModel:
    """
        Eine Klasse, die die Daten der MainView bündelt und Logik aus der MainView heraushät.
    """
    def __init__(self):
        self.value_red:tkinter.IntVar = tkinter.IntVar()
        self.value_green:tkinter.IntVar = tkinter.IntVar()
        self.value_blue:tkinter.IntVar = tkinter.IntVar()

    @staticmethod
    def __to_hex(value: int):
        """
            Eine Hilfsmethode um bytes in hexadezimalzahlen umzuwandeln.
        """
        chars:list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        return chars[math.floor(value/16)] + chars[math.floor(value%16)]


    def get_mixed_color(self) -> str:
        """
            Liest die Farbwerte aus und wandelt sie in einen string um der die farbe in hexadezimal repräsentiert.
        """
        res:str = '#'
        res += self.__to_hex(self.value_red.get())
        res += self.__to_hex(self.value_green.get())
        res += self.__to_hex(self.value_blue.get())
        return  res

import  tkinter

window = MainWindow()
window.mainloop()

"""
def button1_callback():
    print("test")

def button_close_callback():
    try:
        window.destroy()
    except tkinter.TclError:
        pass


button1:tkinter.Button =  tkinter.Button(window, width=10, height=10, command=button1_callback)
button1.place(x=10, y=10, width=30, height=30)
button1.place(bordermode="inside")
button_close:tkinter.Button =tkinter.Button(window, width=10, height=10, bg='red', command=button_close_callback)
button_close.place(x=100, y=10, width=30, height=30)

def entry_text_changed(string1:str, string2:str, string3:str):
    print(entry_text.get())

entry_text:tkinter.Variable = tkinter.Variable()
entry_text.trace_add("write", entry_text_changed)

entry_1:tkinter.Entry = tkinter.Entry(textvariable=entry_text)
entry_1.place(x=150, y=10, width=100, height=50)

"""