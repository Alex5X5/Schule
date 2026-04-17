from Programms.MDbMonitor.Services.ApiService import ApiService

base_url:str = "http://192.168.100.120/db-api"
api = ApiService(base_url)
for location in api.locations:
    print(location.name)

