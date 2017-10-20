import requests
import httplib

#Need to use HTTP 1.0 - HTTP 1.1 does nto return the internal IP
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'


#set URL here. 
url = 'http://yourURLhere'

# code to get 301 redirect and return internal IP address if vulnerable
loc = requests.get(url, allow_redirects=False)
print('-------------')
print(loc.headers['Location'])
print('-------------')
