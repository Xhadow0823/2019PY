import requests
from bs4 import BeautifulSoup

target = 'https://data.gov.tw/news'
rsp = requests.get(target)
soup = BeautifulSoup(rsp.content.decode('utf-8'))
tb = soup.find('table', class_='table table-hover table-striped sticky-enabled').tbody
for tr in tb.find_all('tr'):
    print(tr.td.text, tr.a.text)