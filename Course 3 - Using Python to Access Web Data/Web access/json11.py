import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input("Enter location: ")
#url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_327080.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#headers = dict(uh.getheaders())
#print('Retrieved', len(data) + len(headers), 'characters')

info = json.loads(data)

count = 0
total = 0
for item in info['comments']:
    #print('Name', item['name'])
    #print('Count', item['count'])
    count = count + 1
    total = total + item['count']
print("Count:", count)
print("Sum:", total)
