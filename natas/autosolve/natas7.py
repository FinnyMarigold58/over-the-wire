#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth=(username, password))

content = response.text

print(content)

# print(re.findall('The password for natas7 is (.*)',content)[0])