import re
import json
import requests
from urllib2 import urlopen

def getIPInfo():
	url = 'http://ipinfo.io/json'
	response = urlopen(url)
	data = requests.get('http://ipinfo.io').json()

	IP=data['ip']
	org=data['org']
	city = data['city']
	country=data['country']
	region=data['region']
	loc = data['loc']

	return data
