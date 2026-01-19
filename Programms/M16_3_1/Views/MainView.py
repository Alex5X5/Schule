import tkinter

from Programms.M16_3_1.ViewModels import MainViewModel


class MainView(tkinter.Frame):

    def __init__(self, master:tkinter.Misc):
        super().__init__(master, bg='white')

        #erstelle view_model
        self.view_model: MainViewModel.MainViewModel = MainViewModel.MainViewModel()

        #erstelle frames als container für restliche widgets
        self.main_frame:tkinter.Frame = tkinter.Frame(self, bg='white')
        self.sliders_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')
        self.labels_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')
        self.rectangles_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')
        self.mixed_frame:tkinter.Frame = tkinter.Frame(self.main_frame, bg='white')

        #erstelle die slider
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

        #sertelle die text labels mit den Beschreibungen
        self.label_red:tkinter.Label = tkinter.Label(self.labels_frame, text='red', bg='white')
        self.label_green:tkinter.Label = tkinter.Label(self.labels_frame, text='green', bg='white')
        self.label_blue:tkinter.Label = tkinter.Label(self.labels_frame, text='blue', bg='white')

        #erstelle die Rechtecke für alle Farben
        self.rectangle_red:tkinter.Frame = tkinter.Frame(self.rectangles_frame, bg='red')
        self.rectangle_green:tkinter.Frame = tkinter.Frame(self.rectangles_frame, bg='green')
        self.rectangle_blue:tkinter.Frame = tkinter.Frame(self.rectangles_frame, bg='blue')
        self.rectangle_mixed:tkinter.Frame = tkinter.Frame(self.mixed_frame)

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
        self.main_frame.grid_columnconfigure(0, weight=5)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=2)
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=2)

        #setzen der grids aller frames, für die jeweiligen Gruppen an widgets
        for component in [self.sliders_frame, self.labels_frame, self.rectangles_frame, self.mixed_frame]:
            for i in range(7):
                component.grid_rowconfigure(i, weight=5 if i%2==0 else 1)
            component.grid_columnconfigure(0, weight=1)
            component.grid_columnconfigure(1, weight=10)
            component.grid_columnconfigure(2, weight=1)


    def grid_components(self):
        #plazieren aller widgets mit der grid() methode
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
        #ein callback, das bei Veränderung der Slider aufgerufen wird.
        #ruft get_mixed_color() des view_model auf und updated den mixed_frame
        self.rectangle_mixed.configure(bg=self.view_model.get_mixed_color())