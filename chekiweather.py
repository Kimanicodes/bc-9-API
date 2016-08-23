#!usr/bin/env/python
import urllib2
import json
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import click


click.clear()
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

cprint(figlet_format('Cheki', font='starwars'),
       'yellow', 'on_blue', attrs=['bold'])
baseurl = "http://api.openweathermap.org/data/2.5/weather"
key = '=2bc3e79bb974a007818864813f53fd35'

with click.progressbar(range(200),
                       label="Loading Cheki Weather",
                       fill_char=click.style('#',
                                             fg='red', bg='black')) as prog_bar:
    for i in prog_bar:
        pass


@click.command()
def get_cities():
    cities = []
    count = 0
    while count < 5:
        cityp = raw_input('Enter at least five city names: \n')
        cities.append(str(cityp))
        count += 1
    return weather_api_fun(cities)


def weather_api_fun(cities):
    click.echo('=' * 60)
    click.echo('City'.ljust(15) + 'Description'.ljust(20) +
               'Temperature'.ljust(16) + 'Country'.ljust(16))
    click.echo('=' * 60)
    for city in cities:
        result = baseurl + '?q=' + city + '&units=metric' + '&APPID' + key
        # click.echo(result)
        # click.echo(cities)
        result2 = urllib2.urlopen(result).read()
        data = json.loads(result2)
        try:
            click.echo(city.ljust(15) +
                       str(data['weather'][0]['description']).ljust(20).title() +
                       str(data['main']['temp']).ljust(20) +
                       data['sys']['country'].ljust(16))
        except KeyError:
            click.echo("You have entered an invalid City Name")
