import sqlite3
from lib2to3.fixes.fix_imports2 import MAPPING
from typing import Any

from Programms.Mod.DesignTimeService import DesignTimeService


class DatabaseCollection:

    def __init__(self, db_context, data_type:type):
        self.db_context:'DatabaseContext' = db_context
        self.data_type:type = data_type
        self.__mapped_data_type:bool = False
        self.type_mapping:list[tuple[str, type]] = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):  # for assignment: obj[i] = value
        self.data[index] = value

    def __delitem__(self, index):  # for deletion: del obj[i]
        del self.data[index]

    @property
    def table_name(self) -> str:
        return self.data_type.__class__.__name__+'s'

    def map_data_type(self) -> list[tuple[str, type]]:
        if self.__mapped_data_type:
            return self.type_mapping
        mapping: list[tuple[str, type]] = []
        dummy_object = object()
        self.data_type.__init__(dummy_object)
        data_type_properties:dict[str, Any] = dummy_object.__dict__
        for prop in data_type_properties.keys():
            self.create_column_command(prop, data_type_properties[prop])
        DesignTimeService.register_data_type(self.data_type)
        return []

    def create_table_creation_command(self) -> str:
        return f'CREATE TABLE {self.table_name}'

    def create_column_creation_command(self, mapping:list[tuple[str, type]], prop:str, value:Any) -> str:
        if isinstance(value, list):
            pass
        if isinstance(value, int):
            mapping.append((prop, int))
            if self.column_exists(prop):
                return 'SELECT 1'
            else:
                return f'ALTER TABLE {self.table_name} DROP COLUMN {prop}'
        elif isinstance(value, str):
            pass
        elif DesignTimeService.is_type_registered(data_type_properties[prop].__class__):
            mapping.append()

    def column_exists(self, column_name:str) -> bool:
        with self.db_context.open_connection() as conn:
            cursor:sqlite3.Cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(my_table)")
            columns:list[str] = [row[1] for row in cursor.fetchall()]
            return column_name in columns

