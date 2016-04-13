# http://requests.readthedocs.org/en/master/
# pip install requests
# https://docs.python.org/2/library/json.html
# pip install json
import json
import requests

url = 'http://192.168.11.17:8080/springwebapp/rest/contact'
payload = {'firstName': 'myname', 'lastName': 'mylast', 'email':'myname@mylast.com'}

r = requests.post(url, json=payload)
print(r.text)
