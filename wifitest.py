import re
import json
import requests
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
loc = data['loc']

print requests.get('http://ipinfo.io').json()
print 'Your IP detail\n '
print 'Location: '.format(loc)