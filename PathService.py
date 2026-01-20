import os
import sys
from pathlib import Path

class PathService:

    def __init__(self, module_name:str):
        self.module_name:str = module_name if module_name.startswith('M') else 'M'+module_name

    @property
    def bundled_app_files_path_string(self) -> str:
        return str(os.path.join(getattr(sys, '_MEIPASS'))
            if hasattr(sys, '_MEIPASS') and getattr(sys, 'frozen', False)
                else str(os.path.dirname(os.path.abspath(__file__))))

    @property
    def assets_path_string(self) -> str:
        return os.path.join(self.bundled_app_files_path_string, 'Assets')

    @property
    def module_path_string(self) -> str:
        return os.path.join(self.bundled_app_files_path_string, 'Programms', self.module_name)

    @property
    def run_file_path_string(self) -> str:
        return self.module_path('Run.py')

    @staticmethod
    def __could_be_file(path: str) -> bool:
        common_extensions: list[str] = ['.py', '.txt']
        if any(path.endswith(extension) for extension in common_extensions):
            return True
        if path.endswith(os.pathsep):
            return False
        last_part: str = path.split(os.pathsep)[-1]
        if os.extsep in last_part:
            return True
        return False

    @staticmethod
    def __could_be_path(path: str) -> bool:
        try:
            Path(path)
            return not PathService.__could_be_file(path)
        except:
            return False

    @staticmethod
    def __ensure_path_exists(path:str) -> str:
        parent_dir = os.path.dirname(path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        if not os.path.exists(path):
            if PathService.__could_be_file(path):
                open(path, 'w').close()
            elif PathService.__could_be_path(path):
                os.makedirs(path)
        return path

    def assets_path_insecure(self, filename:str) -> str:
        return self.project_path(os.path.join('Assets', filename))

    def assets_path(self, filename:str) -> str:
        return self.__ensure_path_exists(self.assets_path_insecure(filename))

    def module_path_insecure(self, filename: str) -> str:
        return os.path.join(self.module_path_string , filename)

    def module_path(self, filename: str) -> str:
        return self.__ensure_path_exists(self.module_path_insecure(filename))

    def project_path_insecure(self, filename: str) -> str:
        return os.path.join(self.bundled_app_files_path_string, filename)

    def project_path(self, filename: str) -> str:
        return self.__ensure_path_exists(self.project_path_insecure(filename))

    def schemata_path_insecure(self, filename: str) -> str:
        return self.assets_path(os.path.join('GeneratorSchemata', filename))

    def schemata_path(self, filename: str) -> str:
        return self.schemata_path_insecure(filename)
