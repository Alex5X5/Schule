import inspect
import os

from importlib import import_module

import Paths
from Paths import PathHelper

import Run


def __gen_stub(module_number:str):
    path_helper:PathHelper = PathHelper(module_number)
    #create the __init__.py file in the new directory
    init_file_path:str = Paths.ensure_path_exists(path_helper.module_path('__init__.py'))
    #create the Run<module number>.py file in the new directory
    run_file_path:str = Paths.ensure_path_exists(path_helper.module_path('Run.py'))
    with open(run_file_path, 'w') as file_handle:
        file_handle.write("""print('hello world!')""")
    #create the summary.txt file in the new directory
    summary_file_path:str = Paths.ensure_path_exists(path_helper.module_path('Summary.txt'))
    #ask for a summary of this module and write it to the summary.txt file
    with open(summary_file_path, 'w') as file_handle:
        file_handle.write(input("enter summary"))


def __run(module_number:str):
    try:
        #try to dynamically import the module
        module = import_module("Programms."+module_number+'.Run')
        for name, obj in inspect.getmembers(module):
            # Check if the line is callable (e.g., function, method, etc.)
            if callable(obj):# and not inspect.isfunction(obj):
                # Call the function or method
                obj()
    except ModuleNotFoundError as e:
        #generate the needed module and re-run the module
        print(f'module {module_number} was not found')
        __gen_stub(module_number)
        __run(module_number)


def __get_module(path_to_check: str) -> str:
    if path_to_check != '':
        with open('last_module', 'w') as file_handle:
            file_handle.write(path_to_check)
            return path_to_check
    else:
        with open('last_module', 'r') as file_handle:
            return file_handle.readlines()[0]


if __name__ == '__main__':
    __run(__get_module(input('enter module name:\n')))
    print('finished main')