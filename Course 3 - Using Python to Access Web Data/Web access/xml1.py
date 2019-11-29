import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input("Enter location: ")
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_327079.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

numlist = list()
comment = tree.findall('comments/comment')
# counts = tree.findall('.//count')
count = 0
for item in comment:
    num_str = item.find('count').text
    num = int(num_str)
    numlist.append(num)
    count = count + 1
print("Count:", count)
print("Sum:", sum(numlist))

#for n in counts:
    #print(n[count])
