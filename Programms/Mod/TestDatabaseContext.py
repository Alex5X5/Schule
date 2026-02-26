from dataclasses import dataclass

from Programms.Mod.DatabaseCollection import DatabaseCollection
from Programms.Mod.DatabaseContext import DatabaseContext


@dataclass
class User:

    id:int
    name:str
    age:int


@dataclass
class Job:

    id:int
    worker:User


class TestDatabaseContext(DatabaseContext):

    def __init__(self):
        super().__init__()
        self.users:DatabaseCollection = DatabaseCollection(User)
        self.devices:DatabaseCollection = DatabaseCollection(Job)
