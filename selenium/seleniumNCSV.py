cityUrls = {'基隆市' : 'Keelung_City.htm',
'台北市' : 'Taipei_City.htm',
'新北市' : 'New_Taipei_City.htm',
'桃園市' : 'Taoyuan_City.htm',
'新竹市' : 'Hsinchu_City.htm'}

def f氣溫(cities, t=0):  #0:白天, 1:晚上
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import re
    import csv
    web = webdriver.Chrome()
    base = 'https://www.cwb.gov.tw/V7/forecast/taiwan/'
    first = True
    with open(('晚上' if t else '白天')+'氣溫.csv', 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for cityN, cityU in cities.items():
            web.get(base+cityU)
            tb = BeautifulSoup(web.page_source).find_all('table', class_='FcstBoxTable01')[1]
            if first:
                #print(['城市']+[re.search(r'\d+/\d+', tb.thead.find_all('th')[i].text).group() for i in range(1,8)])
                writer.writerow(['城市']+[re.search(r'\d+/\d+', tb.thead.find_all('th')[i].text).group() for i in range(1,8)])
                first = False
            #print([cityN]+[re.search(r'\d+ ~ \d+', tp.text).group() for tp in tb.tbody.find_all('tr')[t].find_all('td')])
            writer.writerow([cityN]+[re.search(r'\d+ ~ \d+', tp.text).group() for tp in tb.tbody.find_all('tr')[t].find_all('td')])
            #print('\n'+'-----'*4)
    web.close()


def f天氣(cities, t=0):  #0:白天, 1:晚上
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import re
    import csv
    web = webdriver.Chrome()
    base = 'https://www.cwb.gov.tw/V7/forecast/taiwan/'
    first = True
    with open(('晚上' if t else '白天')+'天氣.csv', 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for cityN, cityU in cities.items():
            web.get(base+cityU)
            tb = BeautifulSoup(web.page_source).find_all('table', class_='FcstBoxTable01')[1]
            if first:
                #print(['城市']+[re.search(r'\d+/\d+', tb.thead.find_all('th')[i].text).group() for i in range(1,8)])
                writer.writerow(['城市']+[re.search(r'\d+/\d+', tb.thead.find_all('th')[i].text).group() for i in range(1,8)])
                first = False
            #print([cityN]+[w['alt'] for w in tb.tbody.find_all('tr')[0].find_all('img')])
            writer.writerow([cityN]+[w['alt'] for w in tb.tbody.find_all('tr')[0].find_all('img')])
            #print('\n'+'-----'*4)
    web.close()

f氣溫(cityUrls)
f氣溫(cityUrls, 1)
f天氣(cityUrls)
f天氣(cityUrls, 1)