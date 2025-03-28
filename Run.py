import functools
import importlib
import inspect

from importlib import import_module

def assets_path():
    assets = import_module('M03')

def __run(module_number:str):
    module = import_module('M'+module_number+'.Run','Run')
    #module.__getattribute__('run')()
    for name, obj in inspect.getmembers(module):
        # Check if the object is callable (e.g., function, method, etc.)
        if callable(obj) and not inspect.isfunction(obj):
            #print(f"Calling {name}()")
            obj()  # Call the function or method

if __name__ == '__main__':
    __run(input('enter module name:\n'))
    print('finished main')