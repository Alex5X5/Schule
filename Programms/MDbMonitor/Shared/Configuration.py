from Programms.MDbMonitor.lib.DependencyInjector import DpiEntryPoint


class Configuration:

    @DpiEntryPoint
    def __init__(self):
        pass

    @property
    def base_url(self) -> str:
        return "http://192.168.100.120/db-api"