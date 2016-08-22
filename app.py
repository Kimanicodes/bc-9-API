#!usr/bin/env/python
import urllib2
import json
import sys
import os
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

os.system('clear')
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

cprint(figlet_format('Cheki', font='starwars'),
       'yellow', 'on_blue', attrs=['bold'])
baseurl = "http://api.openweathermap.org/data/2.5/weather"
key = '=2bc3e79bb974a007818864813f53fd35'

cities = []
count = 0
while count < 5:
    city = raw_input('Enter at least five city names: \n')
    cities.append(str(city))
    count += 1


def weather_api_func(cities):
    print('=' * 60)
    print('City'.ljust(15) + 'Description'.ljust(20) +
          'Temperature'.ljust(16) + 'Country'.ljust(16))
    print('=' * 60)
    for city in cities:
        result = baseurl + '?q=' + city + '&units=metric' + '&APPID' + key
        result = urllib2.urlopen(result).read()
        data = json.loads(result)
        try:
            print (city.ljust(15).title() +
                   str(data['weather'][0]['description']).ljust(20).title() +
                   str(data['main']['temp']).ljust(20) +
                   data['sys']['country'].ljust(16))
        except KeyError:
            print("You have entered an invalid City Name")


if __name__ == "__main__":
    weather_api_func(cities)
