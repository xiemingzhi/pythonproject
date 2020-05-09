# http://requests.readthedocs.org/en/master/
# pip install requests
# https://docs.python.org/2/library/json.html
# pip install json
import json
import requests

#requests.exceptions.SSLError: HTTPSConnectionPool(host='jsonplaceholder.typicode.com', port=443): Max retries exceeded with url: /todos?_limit=1 (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available."))
url = 'http://jsonplaceholder.typicode.com/todos?_limit=1'
payload = {'firstName': 'myname', 'lastName': 'mylast', 'email':'myname@mylast.com'}

r = requests.post(url, json=payload)
print(r.text)
