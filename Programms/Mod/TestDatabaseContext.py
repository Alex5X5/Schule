from dataclasses import dataclass

from Programms.Mod.DatabaseCollection import DatabaseCollection
from Programms.Mod.DatabaseContext import DatabaseContext


@dataclass
class User:
    id:int
    name:str
    age:int


@dataclass
class Device:
    id:int
    owner:User


class TestDatabaseContext(DatabaseContext):

    def __init__(self):
        super().__init__('database.sqlite3')
        self.users:DatabaseCollection = DatabaseCollection(self, User)
        self.devices:DatabaseCollection = DatabaseCollection(self, Device)
