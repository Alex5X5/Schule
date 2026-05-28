class Line:

    def __init__(self, id:str, name:str):
        self.id:str = id
        self.name:str = name

    def __str__(self):
        return f"Line[id={self.id}, name={self.name}]"