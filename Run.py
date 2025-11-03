def __run(module_number:str):
    print('starting Run.py')
    cmd = 'M'+module_number+'/Run.py'
    exec(open(cmd).read())
    print('finished run')

if __name__ == '__main__':
    __run(input('enter module name:\n'))
    print('finished main')