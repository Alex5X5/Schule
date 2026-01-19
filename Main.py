import inspect
import os

from importlib import import_module
from os.path import pathsep

import PathService
from PathService import PathService


def __gen_stub(module_number:str):
    path_helper:PathService = PathService(module_number)
    path_helper.module_path('__init__.py')
    run_file_path:str = path_helper.module_path('Run.py')
    with open(run_file_path, 'w') as file_handle:
        file_handle.write("""print('hello world!')""")
    summary_file_path:str = PathService.ensure_path_exists(path_helper.module_path('Summary.txt'))
    with open(summary_file_path, 'w') as file_handle:
        file_handle.write(input("enter summary"))

def __run(module_number:str):
    path_helper:PathService = PathService(module_name)
    cmd = path_helper.module_path_string('Run.py')
    try:
        with open(cmd) as file_handle:
            print('starting Run.py')
            exec(file_handle.read())
        print('finished run')
    except FileNotFoundError:
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
            print("getting last module")
            return file_handle.readlines()[0]


if __name__ == '__main__':
    module_name: str = __get_module(input('enter module name:\n'))
    print(f"running module \"{module_name}\"")
    __run(module_name)
    print('finished main')