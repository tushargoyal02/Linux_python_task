#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
url=raw_input('Enter the website you want to access:')
req=requests.get('https://'+url)
# req text is used to get the data present in Url
data=req.text
print data

#
soup=BeautifulSoup(data)
#finfing all (a) in html to extract the URL
for link in soup.find_all('a'):
	#to print all a and href link in next step (Will all link in <a href=""link>:)
	print link.get('href')
	
