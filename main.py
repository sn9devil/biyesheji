import requests
import time
from bs4 import BeautifulSoup
from data import new_insert,find_new
from now_time import now_time

while(1):
    html = r'http://news.163.com/'
    response = requests.get(html)
    soup = BeautifulSoup(response.text,'lxml')
    news = soup.select('div .mod_top_news2 > .top_news_title a')

    for i in news:
        url = i.get('href')
        print(url)
        if(find_new(url)):
            print('未更新')
        else:
            new = i.text
            date = now_time()
            new_insert(new,url,date)
            print('录入')
    time.sleep(20)

