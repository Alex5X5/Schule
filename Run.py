import functools
import importlib
import inspect
import os

from importlib import import_module

def assets_path():
    assets = import_module('M03')

def __run(module_number:str):
#    module = import_module('M'+module_number+'.Run','Run')
#    s = 'python M'+module_number+'/Run.py'
#    os.system(s)

    cmd = 'M'+module_number+'/Run.py'
    exec(open(cmd).read())
    return

#    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, creationflags=CREATE_NEW_CONSOLE)

    out, err = p.communicate()
    result = str(out).split('\n')
    for lin in result:
        if not lin.startswith('#'):
            print(lin.removeprefix('b\'').removesuffix('\\r\\n\''))
#    for name, obj in inspect.getmembers(module):
#        if callable(obj) and not inspect.isfunction(obj):
#            obj()  # Call the function or method

if __name__ == '__main__':
    __run(input('enter module name:\n'))
    print('finished main')