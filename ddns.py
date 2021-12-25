
import requests
import dns.resolver
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
delay = 610.0

query = {'hostname':hostname}
url = 'https://'+user+':'+token+'@api.cp.easydns.com/dyn/generic.php'

print('DDNS updater starting for hostname ' + hostname)

while True:
	current_ip = get('https://api.ipify.org', timeout=5.0).content.decode('utf8')
	res = dns.resolver.resolve(hostname, 'A')
	for item in res:
		if (str(current_ip) != str(item)):
			print('Current ip is ' + str(current_ip))
			print('A record is ' + str(item))
			print('A record needs update')
			response = requests.get(url, params=query)
			print(response.text)

	time.sleep(delay)
