
# 1  парсинг списка всех игр которым редакция стоп гейм паставила оценку изумительно

import requests
from  bs4 import  BeautifulSoup as BS
r = requests.get("https://stopgame.ru/review/new/izumitelno/p1")
html = BS(r.content,'html.parser')
for el in html.select(".items > .article-summary"):
    title = el.select('.caption > a')
    print(title[0].text)
# мы парсили одну страницу



# 2 чтобы парсить всю страницу

import requests
from  bs4 import  BeautifulSoup as BS
page = 1
while True:
    r = requests.get("https://stopgame.ru/review/new/izumitelno/p1"+str(page))
    html = BS(r.content,'html.parser')
    if (len(items)):
        for el in html.select(".items > .article-summary"):
            title = el.select('.caption > a')
            print(title[0].text)
        page += 1
    else:
        break

