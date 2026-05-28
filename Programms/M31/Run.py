from Programms.MDbMonitor.Api.Services import ApiService

base_url:str = "https://192.168.100.120/"
#response = requests.get(f"{base_url}/topass-api/card-sets/trucks/A4")
#print(response.status_code)
#print(response.text)
#response = requests.get(f"{base_url}/topass-api/card-sets/cars")
#print(response.status_code)
#cars = json.loads(response.text).get("items")
#for car in cars:
#    print(car)

api = ApiService(base_url)
for location in api.locations:
    print(location.name)

