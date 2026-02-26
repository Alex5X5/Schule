import os
import pathlib
from io import TextIOWrapper

import PathService

class GeneratorService:

    def __init__(self, module_number:str):
        self.path_service:PathService.PathService = PathService.PathService(module_number)

    def __genrate_base(self):
        self.path_service.module_path('__init__.py')
        run_file_path:str = self.path_service.module_path('Run.py')
        with open(run_file_path, 'w') as file_handle:
            file_handle.write("""print('hello world!')""")
        summary_file_path:str = self.path_service.module_path('Summary.txt')
        with open(summary_file_path, 'w') as file_handle:
            file_handle.write(input("enter summary"))

    def generate(self):
        print('select a schema')
        print('available schemata are:')
        schemata:list[str] = os.listdir(self.path_service.schemata_path(''))
        for i, path in enumerate(schemata):
            print(f'  {i}:{pathlib.Path(path).stem}')
        while True:
            try:
                schema_name_str:str = input('enter a number\n')
                if schema_name_str == '':
                    self.__genrate_base()
                    break
                input_number:int = int(schema_name_str)
                if input_number < 0:
                    print('not a number')
                    continue
                if input_number > len(schemata) - 1:
                    print('input out of range')
                    continue
                self.create_files(schemata[input_number])
                break
            except ValueError:
                print('invalid choice')

    def create_files(self, schema:str):
        with open(self.path_service.schemata_path(schema), 'r') as read_file_handle:
            lines:list[str] = read_file_handle.readlines()
            index:int = 0
            write_file_handle:TextIOWrapper | None = None
            buffer:list[str] = []
            while index < len(lines):
                if lines[index].startswith('#file:'):
                    if write_file_handle is not None:
                        if not write_file_handle.closed:
                            write_file_handle.write(''.join(buffer))
                            buffer = []
                            write_file_handle.close()
                    write_file_handle = open(self.path_service.module_path(lines[index].removeprefix('#file:').strip('\n')), 'w')
                    index += 1
                    continue
                buffer.append(lines[index].replace('$(Module)', self.path_service.module_name))
                if index == len(lines) - 1:
                    if write_file_handle is not None:
                        if not write_file_handle.closed:
                            write_file_handle.write(''.join(buffer))
                            write_file_handle.close()
                index += 1
