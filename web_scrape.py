import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.mirror.co.uk/sport/football/transfer-news/liverpool-alexis-macallister-transfer-brighton-30106200')
 
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

s = soup.find('div', class_='entry-content')
content = s.find_all('p')
 
print(content)