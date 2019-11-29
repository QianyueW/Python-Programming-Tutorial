from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = raw_input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Karandeep.html'
count = int(input('Enter count: ')) + 1
position = int(input('Enter position: '))

for i in range(count):
    print('retrieving: ', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position-1].get('href', None)
