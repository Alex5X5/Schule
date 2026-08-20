import tkinter as tk
from tkinter import ttk

def checkKomboOben():
    if bool_oben.get():
        lbl_oben.config(background=color_on.get())
    else:
        lbl_oben.config(background=color_off.get())
    pass

def checkKomboUnten():
    if bool_unten.get():
        lbl_unten.config(background=color_on.get())
    else:
        lbl_unten.config(background=color_off.get())
    pass

window = tk.Tk()
window.title("Checkbutten, Combobox und Farben")
window.geometry("600x200")
window.minsize(600, 200)

color_on = tk.StringVar(value="green")
color_off = tk.StringVar(value="red")

bool_oben = tk.BooleanVar(value=True)
bool_unten = tk.BooleanVar(value=False)

window.columnconfigure(0, minsize=50)
window.columnconfigure(1, minsize=150)
window.columnconfigure(2, minsize=150)
window.columnconfigure(3, minsize=150)

# COLMN 1
chk_oben = tk.Checkbutton(window, text="Oben", variable=bool_oben, command=checkKomboOben)
chk_oben.grid(row=0, column=0)
chk_unten = tk.Checkbutton(window, text="Unten", variable=bool_unten, command=checkKomboUnten)
chk_unten.grid(row=1, column=0)

# COLMN 2
lbl_oben = tk.Label(window, width=10, background=color_on.get())
lbl_oben.grid(row=0, column=1)
lbl_unten = tk.Label(window, width=10, background=color_off.get())
lbl_unten.grid(row=1, column=1)

# COLMN 2
lbl_dr_oben = tk.Label(window, text="Farbe für den Zustand AN:")
lbl_dr_oben.grid(row=0, column=2)
lbl_dr_unten = tk.Label(window, text="Farbe für den Zustand AUS:")
lbl_dr_unten.grid(row=1, column=2)

# COLMN 4
dr_an = ttk.Combobox(window, textvariable=color_on)
dr_an.grid(row=0, column=3)
dr_aus = ttk.Combobox(window, textvariable=color_off)
dr_aus.grid(row=1, column=3)

# BTN END
lbl_dr_unten = tk.Label(window)
lbl_dr_unten.grid(row=2, column=2)
end_btn = tk.Button(window, width=10, command=window.destroy, text="Beenden")
end_btn.grid(row=3, columnspan=4)

# Configure drp
colors = ["red", "green", "blue", "lime"]
dr_an["values"] = colors
dr_aus["values"] = colors

window.mainloop()