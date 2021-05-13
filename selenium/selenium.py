from bs4 import BeautifulSoup
from selenium import webdriver

target = 'https://www.cwb.gov.tw/V7/observe/real/NewObs.htm'
cid = {u'基隆':10017, u'台北市':63}
web = webdriver.Chrome()


def printTable(city):
    global cid, web, target
    web.get(target)
    web.find_element_by_xpath('//a[@code="{}"]'.format(cid[city])).click()
    soup = BeautifulSoup(web.page_source)
    for h in soup.find('table', id=cid[city]).thead.tr.find_all('th')[1:]:
        print(h.text, end=' ')
    for tr in soup.find('table', id=cid[city]).tbody.find_all('tr'):
        for td in tr.find_all('td')[1:]:
            print(td.text, end=' ')
        print()


printTable('基隆')
printTable('台北市')