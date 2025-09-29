from io import FileIO
import os
import sys
from io import FileIO
from os.path import dirname

bundled_app_files_path_string = os.path.join(getattr(sys, '_MEIPASS') if hasattr(sys,'_MEIPASS') and getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__)))

def ensure_path_exists(path:str) -> str:
    """
        checks whether a path exists and creates it in case it doesn't.
        returns the directory path if the given path is a path to a file.

        :param path: the name of the path
        :return:
    """
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    return path

def assets_path(filename:str) -> str:
    return ensure_path_exists(bundled_app_files_path_string + '\\Assets\\' + filename)

def project_path(filename:str) -> str:
    """
        :param filename:
        :return:
    """
    return ensure_path_exists(bundled_app_files_path_string + '\\' + filename)

def module_path(filename:str, module_name:str) -> str:
    return ensure_path_exists(bundled_app_files_path_string + '\\Programms\\' + module_name + '\\' + filename)