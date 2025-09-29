import inspect
import os

from importlib import import_module

import Paths


def __gen_stub(module_number:str):
    #create the directory
    Paths.ensure_path_exists(Paths.project_path('Programms\\' + module_number))
    #create the __init__.py file in the new directory
    Paths.ensure_path_exists(Paths.project_path('Programms\\' + module_number + '\\__init__.py'))
    #create the Run<module number>.py file in the new directory
    Paths.ensure_path_exists(Paths.project_path('Programms\\' + module_number + '\\Run'+module_number+'.py'))
    #create the summary.txt file in the new directory
    Paths.ensure_path_exists(Paths.project_path('Programms\\' + module_number + '\\Summary.txt'))
    #with open(Paths.project_path('Programms\\' + module_number + '\\Run.Py'), 'w') as file_handle:
    #    pass
    #with open(Paths.project_path('Programms\\' + module_number + '\\__init__.py'), 'w') as file_handle:
    #    pass
    #ask for a summary of this module and write it to the summary.txt file
    #with open(Paths.project_path('Programms\\' + module_number + '\\Summary.txt'), 'w') as file_handle:
    #    file_handle.write(input("enter summary"))

def __run(module_number:str):
    module = import_module("Programms."+module_number+'.Run')
    try:
        #try to dynamically import the module

        for name, obj in inspect.getmembers(module):
            # Check if the line is callable (e.g., function, method, etc.)
            if callable(obj):# and not inspect.isfunction(obj):
                # Call the function or method
                obj()
    except ModuleNotFoundError as e:
        #generate the needed module and re-run the module
        print(f'module {module_number} was not found')
        __gen_stub(module_number)

if __name__ == '__main__':
    __run(input('enter module name:\n'))
    print('finished main')