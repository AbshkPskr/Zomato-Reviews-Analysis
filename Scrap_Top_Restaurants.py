import numpy as np
import pandas as pd
from Get_Page_Html import GetPageHtml
from Scrap_Reviews import ScrapReviews
import os

url = "https://www.zomato.com/ncr/top-restaurants"
top_restaurants_html = GetPageHtml(url)
print(top_restaurants_html)
main_div = top_restaurants_html.find('div',{'class':"bke1zw-0 cMipmx"})

restaurants_urls = []
for divs in main_div.children:
    url = divs.contents[0].contents[1].contents[0]['href'].split("?")[0]
    restaurants_urls.append(url)


def getdata(rest):
    ScrapReviews(rest)
    # columns = ['name','rating','reviews']
    # df = pd.DataFrame(columns = columns)
    # for value in dic['reviews']:
    #     df = df.append({'name': dic['name'],'rating':dic['rating'],'reviews':value},ignore_index = True)
    # df.to_csv('reviews.csv', mode = 'a', header = False, index=False)

from threading import Thread
for rest in restaurants_urls:
    print(rest)
    th = Thread(target = getdata,args=[rest])
    th.start()
    # getdata(rest)

import time
for i in range(0,10):
    df = pd.read_csv('reviews.csv').drop_duplicates()
    print(df)
    df.to_csv('rr.csv')
    time.sleep(2)