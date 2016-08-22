import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?q="
key = '=2bc3e79bb974a007818864813f53fd35'
cities = ['Nairobi', 'Lagos', 'Washington']
print('=================================================================')
print('City'.ljust(15) + 'Temperature'.ljust(15) + 'Description'.ljust(20))
print('=================================================================')
for city in cities:
    response = requests.get(url + city + '&units=metric' + '&APPID' + key)
    response = json.loads(response.content)
    print(city.ljust(15).title() +
          str(response['main']['temp'].ljust(15)) +
          str(response['weather'][0]['description'].ljust(15)))
