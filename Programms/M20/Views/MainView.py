import tkinter

from Programms.M20.ViewModels import MainViewModel

class MainView(tkinter.Frame):

    def __init__(self, master:tkinter.Misc):
        super().__init__(master, bg='white')

        #erstelle view_model
        self.view_model: MainViewModel.MainViewModel = MainViewModel.MainViewModel()

        #erstelle frames als container für restliche widgets
        self.main_frame:tkinter.Frame = tkinter.Frame(self, bg='orange')
        self.input_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='green')
        self.output_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='red')

        #sertelle die text labels mit den Beschreibungen
        self.label_vorname:tkinter.Label = tkinter.Label(self.input_frame, text='vorname')
        self.label_nachname:tkinter.Label = tkinter.Label(self.input_frame, text='nachname')
        self.label_telefonnummer:tkinter.Label = tkinter.Label(self.input_frame, text='telefonnummer')

        self.button_add:tkinter.Button = tkinter.Button(self.input_frame, text='Kontakt hinzufügen')

        #erstelle die Rechtecke für alle Farben
        self.output_listbox:tkinter.Listbox = tkinter.Listbox(self.output_frame, bg='red')

        #hizufügen des callbacks zu den IntVars des view_model
        self.view_model.value_red.trace_add('write', self.on_color_changed)
        self.view_model.value_green.trace_add('write', self.on_color_changed)
        self.view_model.value_blue.trace_add('write', self.on_color_changed)

        self.grid_configure_components()
        self.grid_components()

    def grid_configure_components(self):
        #setzen des grids des fensters
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=20)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_columnconfigure(2, weight=1)

        #setzen der grids des main_frame
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)


        #setzen der grids aller frames, für die jeweiligen Gruppen an widgets
        for i in range(3):
            i_:int= i*3
            self.input_frame.grid_rowconfigure(i_, weight=1)
            self.input_frame.grid_rowconfigure(i_+1, weight=2)
            self.input_frame.grid_rowconfigure(i_+2, weight=4)
        self.input_frame.grid_columnconfigure(0,weight=3)
        self.input_frame.grid_columnconfigure(1,weight=2)
        self.input_frame.grid_columnconfigure(2,weight=3)


    def grid_components(self):
        #plazieren aller widgets mit der grid() methode
        self.main_frame.grid(row=1, column=1, sticky='nsew')

        self.input_frame.grid(row=0, column=0, sticky='nswe')
        self.output_frame.grid(row=1, column=0, sticky='nsew')

        self.label_vorname.grid(row=1, column=1, sticky='nswe')
        self.label_nachname.grid(row=5, column=1, sticky='nswe')
        self.label_telefonnummer.grid(row=5, column=1, sticky='nswe')
        self.button_add.grid(row=7, column=1, sticky='nswe')

    def on_color_changed(self, s1:str, s2:str, s3:str):
        #ein callback, das bei Veränderung der Slider aufgerufen wird.
        #ruft get_mixed_color() des view_model auf und updated den mixed_frame
        self.rectangle_mixed.configure(bg=self.view_model.get_mixed_color())

