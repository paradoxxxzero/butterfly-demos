try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

from butterfly.escapes import html, colors
from random import randint
from json import loads

response = loads(urlopen(
    "http://xkcd.com/info.0.json").read().decode('utf-8'))
last = int(response['num'])
id = randint(0, last)
response = loads(urlopen(
    "http://xkcd.com/%d/info.0.json" % id).read().decode('utf-8'))

print()
print(colors.blue + '#%d ' % id + colors.white +
      response['title'] + colors.reset)
print()
with html():
    print('<img src="%s" alt="%s" />' % (
        response['img'], response['title']))

print()
print(colors.light_white + response['alt'] + colors.reset)
