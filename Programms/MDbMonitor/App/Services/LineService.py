from Programms.MDbMonitor.App.Mapping.LineMapper import LineMapper

from Programms.MDbMonitor.Api.Services.ApiService import ApiService

from libs.DependencyInjection import DpiEntryPoint

class LineService:

    @DpiEntryPoint
    def __init__(self, api:ApiService, mapper:LineMapper) -> None:
        self.api:ApiService = api
        self.mapper:LineMapper = mapper

