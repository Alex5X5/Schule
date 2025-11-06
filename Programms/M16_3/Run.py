import tkinter

from Programms.M16_3  import MyWindow

window:MyWindow.MyWindow = MyWindow.MyWindow()
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