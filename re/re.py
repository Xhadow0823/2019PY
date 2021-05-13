import requests
import re
pattern = r'<tr><td class=\"td-date\">(.*?)</td><td class=\"td-title\"><a href=\"/node/\d*\">(.*?)</a></td> </tr>'
content = requests.get('https://data.gov.tw/news').content.decode('utf-8')
for it in re.findall(pattern, content):
    print(it[0], it[1])