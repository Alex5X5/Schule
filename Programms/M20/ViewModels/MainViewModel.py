import math
import tkinter

class MainViewModel:

    def __init__(self):
        self.value_red:tkinter.IntVar = tkinter.IntVar()
        self.value_green:tkinter.IntVar = tkinter.IntVar()
        self.value_blue:tkinter.IntVar = tkinter.IntVar()

    def entry_text_changed(self, string1: str, string2: str, string3: str):
        print(self.entry_text.get())

    @staticmethod
    def __to_hex(value: int):
        chars:list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        return chars[math.floor(value/16)] + chars[math.floor(value%16)]

    def get_mixed_color(self) -> str:
        res:str = '#'
        res += self.__to_hex(self.value_red.get())
        res += self.__to_hex(self.value_green.get())
        res += self.__to_hex(self.value_blue.get())
        return  res

