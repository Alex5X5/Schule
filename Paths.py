from io import FileIO
import os
import sys

bundled_app_files_path_string = os.path.join(sys._MEIPASS if hasattr(sys,'_MEIPASS') and getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__)))
def assets_path(filename:str) -> str: return bundled_app_files_path_string + '\\Assets\\' + filename