import functools
from typing import Any, Callable

import sqlite3

from Programms.Mod.DatabaseCollection import DatabaseCollection


class DatabaseContext:

    def __init__(self, path:str):
        super().__init__()
        self.path = path

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"{cls.__name__} just derived from DatabaseContext!")
        original_init:Callable[[Any, Any, Any], None] | None = cls.__init__ if '__init__' in cls.__dict__ else None

        @functools.wraps(original_init or cls.__init__)
        def patched_init(self, *args_, **kwargs_):
            if original_init:
                original_init(self, *args_, **kwargs_)
            else:
                super(cls, self).__init__(*args_, **kwargs_)
            properties: dict[str, Any] = self.__dict__
            for prop in properties.keys():
                if isinstance(properties[prop], DatabaseCollection):
                    properties[prop].map_data_type()

        cls.__init__ = patched_init

    def open_connection(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row
        return con