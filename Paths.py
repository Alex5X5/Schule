from io import FileIO
import os

def assets_path(filename:str) -> str: return str(os.path.abspath(__file__)).replace(r'\\',r'/') + '\\..Assets\\' + filename