from setuptools import setup

setup(
    name='ChekiWeather',
    version='0.1.0',
    py_modules=['chekiweather'],
    install_requires=[
        'Click',
        'colorama',
        'termcolor',
        'pyfiglet'
    ],
    entry_points='''
        [console_scripts]
        chekiweather=chekiweather:weather_api_func(cities)
    ''',
)
