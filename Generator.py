import Paths

input('enter module name:\n')


schema_name:str = input('input schema file name: ')
target_module_name:str = input('input target module file name: ')

with open(Paths.assets_path('generator_schema_files\\'+schema_name),'r') as read_file_handle:
    with open(Paths.assets_path(''),'w') as write_file_handle:
        write_file_handle.writelines(read_file_handle.readlines())
