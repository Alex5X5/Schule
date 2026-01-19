import PathService

class GeneratorService:

    def __init__(self, module_number:str):
        self.path_service:PathService.PathService = PathService.PathService(module_number)

    def __genrate_base(self):
        self.path_service.module_path('__init__.py')
        run_file_path:str = self.path_service.module_path('Run.py')
        with open(run_file_path, 'w') as file_handle:
            file_handle.write("""print('hello world!')""")
        summary_file_path:str = PathService.ensure_path_exists(self.path_service.module_path('Summary.txt'))
        with open(summary_file_path, 'w') as file_handle:
            file_handle.write(input("enter summary"))

    def generate(self):
        schema_name:str = input('input schema file name: ')
        target_module_name:str = input('input target module file name: ')

        with open(PathService.schemata_path(schema_name), 'r') as read_file_handle:
            with open(PathService.assets_path(''),'w') as write_file_handle:
                write_file_handle.writelines(read_file_handle.readlines())
