# -*- coding: utf-8 -*-
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import sys
from json import loads
from butterfly.escapes import geolocation, html, colors

geo = geolocation()
if not geo:
    print('Unable to get location')
    sys.exit(1)

lat, lng = geo

response = loads(urlopen(
    'http://api.openweathermap.org/data/2.5/weather?'
    'lat=%f&lon=%f&appid=6a4f7784ba510a145bef45895c6ac4c1' % (
        lat, lng)).read().decode('utf-8'))

print('Curent weather in %s%s%s\n' % (
    colors.white,
    response['name'],
    colors.reset))

temp = response['main']['temp']

print("Temperature: %s%.1f°C %s(%.1f°F)%s" % (
    colors.blue, temp - 273.15,
    colors.light_blue, temp * 9/5 - 459.67, colors.reset))

weather = response['weather'][0]
with html():
    print('<img src="http://openweathermap.org/img/w/%s.png" alt="%s" />' % (
        weather['icon'], weather['main']
    ))

print('%s%s %s%s%s' % (
    colors.white, weather['main'],
    colors.green, weather['description'],
    colors.reset))
