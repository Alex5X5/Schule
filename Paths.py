from io import FileIO
import os
import sys
from io import FileIO
from os.path import dirname
from pathlib import Path

def __could_be_file(path:str) -> bool:
    common_extensions:list[str] = ['.py', '.txt']
    if any(path.endswith(extension) for extension in common_extensions):
        return True
    if(path.endswith(os.pathsep)):
        return False
    last_part:str = path.split(os.pathsep)[-1]
    if(os.extsep in last_part):
        return True
    return False

def __could_be_path(path:str) -> bool:
    try:
        Path(path)
        return not __could_be_file(path)
    except:
        return False


def ensure_path_exists(path:str) -> str:
    """
        checks whether a path exists and creates it in case it doesn't.
        returns the directory path if the given path is a path to a file.

        :param path: the name of the path
        :return:
    """
    if not os.path.exists(path):
        if __could_be_file(path):
            open(path, 'w').close()
        elif __could_be_path(path):
            os.makedirs(path)
    return path

def assets_path(filename:str) -> str:
    return ensure_path_exists(os.path.join(PathHelper.bundled_app_files_path_string, 'Assets', filename))

def project_path(filename:str) -> str:
    """
        :param filename:
        :return:
    """
    return ensure_path_exists(PathHelper.bundled_app_files_path_string + '\\' + filename)

def module_path(filename:str, module_name:str) -> str:
    return ensure_path_exists(PathHelper.bundled_app_files_path_string + '\\Programms\\' + module_name + '\\' + filename)


class PathHelper:
    bundled_app_files_path_string:str = os.path.join(getattr(sys, '_MEIPASS')
        if hasattr(sys, '_MEIPASS') and getattr(sys, 'frozen', False)
        else os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, module_name:str):
        self.module_name:str = module_name
        ensure_path_exists(self.module_path(""))

    def module_path(self, filename: str) -> str:
        return ensure_path_exists(PathHelper.bundled_app_files_path_string + '\\Programms\\' + self.module_name + '\\' + filename)
