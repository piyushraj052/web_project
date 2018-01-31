import urllib2
from bs4 import BeautifulSoup
i=raw_input("Enter the date in (DD/MM/YYYY) format")
j=i.replace('/','')
k=j[:4]+j[6:]
quote_page ='https://www.rediff.com/issues/'+k+'hl.html'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('div', attrs={'id': 'hdtab1'})
name=name_box.text
pr=name.replace('IST','IST\n\n -')
l=pr.index('!')
p=pr[(l+1):]
print ('\n\n'+'Printing the headlines of '+i+'\n\n'+p)
