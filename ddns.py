
import requests
from requests import get

import time
import os
import sys

user = os.getenv('EASYDNS_USER')
if user is None:
		sys.exit('EASYDNS_USER is not set')
token = os.getenv('EASYDNS_TOKEN')
if token is None:
	sys.exit('EASYDNS_TOKEN is not set')
hostname = os.getenv('EASYDNS_HOSTNAME')
if hostname is None:
	sys.exit('EASYDNS_HOSTNAME is not set')
delay = os.getenv('EASYDNS_UPDATE_PERIOD')
if delay is None:
	sys.exit('EASYDNS_UPDATE_PERIOD is not set')

try:
	delay = float(delay)
except:
	exit('EASYDNS_UPDATE_PERIOD is not valid')

if delay < 600:
	sys.exit('EASYDNS_UPDATE_PERIOD must be at least 600 seconds')

# Need some error handling here
ip = get('https://api.ipify.org', timeout=5.0).content.decode('utf8')

query = {'hostname':hostname}
url = 'https://'+user+':'+token+'@api.cp.easydns.com/dyn/generic.php'

# Perform an initial set of the IP
response = requests.get(url, params=query)
print(response.text)

print('Starting DDNS update loop for host '+hostname)
while True:
	time.sleep(delay)
	newIP = get('https://api.ipify.org', timeout=5.0).content.decode('utf8')
	print('new IP is: ' + newIP)
	if (ip != newIP):
		print('IP Needs updating')
		response = requests.get(url, params=query)
		print(response)	
		print(response.text)
	else:
		print('No IP update needed')
