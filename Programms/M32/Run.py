with (open("cursed.py") as file):
    text:str = file.read()
    secret_code = """import ctypes, warnings\n"""\
    + """F = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.c_void_p)\n"""\
    + """@F\n"""\
    + """def call(self, args, kwargs):\n"""\
    + """    return args[0](self)\n"""\
    + """ctypes.cast(id(str), ctypes.POINTER(ctypes.c_void_p))[16] = ctypes.cast(call, ctypes.c_void_p).value\n"""\
    + """warnings.filterwarnings("ignore", category=SyntaxWarning)\n"""
    exec(secret_code + text)