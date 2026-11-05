import os.path

import PathService
from Services.GeneratorService import GeneratorService
from contextlib import chdir

def __run(module_number:str):
    path_helper:PathService.PathService = PathService.PathService(module_name)
    path = path_helper.module_path_insecure('Run.py')
    text: str = ""

    try:
        with open(path) as file_handle:
            text = file_handle.read()
    except FileNotFoundError:
        print(f'module {module_number} was not found')
        GeneratorService(module_number).generate()
        __run(module_number)
    finally:
        print('starting Run.py')
        working_dir:str = os.path.dirname(path)
        with chdir(working_dir):
            exec(text)


def __get_module(path_to_check: str) -> str:
    if path_to_check != '':
        with open('last_module', 'w') as file_handle:
            file_handle.write(path_to_check)
            return path_to_check
    else:
        with open('last_module', 'r') as file_handle:
            return file_handle.readlines()[0]


if __name__ == '__main__':
    module_name: str = __get_module(input('enter module name\nleave empty to run last module:\n'))
    if not module_name.startswith("M"):
        module_name = "M" + module_name
    __run(module_name)
