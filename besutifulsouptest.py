import urllib3
from bs4 import BeautifulSoup
res = urllib3.open("https://www.uno.com.np/uno")
reshtml=res.read()
res.close()

soup=BeautifulSoup(reshtml)
division=soup.find_all('div')

for items in division:
    print(items)