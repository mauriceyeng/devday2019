#a=6
#b=5
#c=a*b
#print(c)

#number=1
#while (number<11):
#    print(number)
#    number=number+1

#a=input()
#print(int(a)*2)

import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.lpu.in')
print(page)
#print(page.text)
soup=BeautifulSoup(page)
portfolio=soup.find("div",{"id":"portfolio"})
print(portfolio)
headlines=portfolio.find.all("div",{"class": "entry-title"})
for heading in headlines:
        print(heading.find("h2").txt)