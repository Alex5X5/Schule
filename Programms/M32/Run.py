

with open("cursed.py") as file:
    for line in file.readlines():
        if line == """"hello world"(print)""":
            print("hello world")
        else:
            exec(line)