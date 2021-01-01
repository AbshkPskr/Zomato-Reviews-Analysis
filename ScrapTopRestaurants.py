import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

r = HTMLSession().get("https://www.zomato.com/ncr/top-restaurants",headers = headers)

r.html.render(sleep=1, keep_page = True, scrolldown = 1)

soup = BeautifulSoup(r.text,'html.parser')
main_div = soup.find('div',{'class':"bke1zw-0 cMipmx"})

restaurants_url = []
count = 1
for divs in main_div.children:
    sec = divs.contents[0]
    # print(sec.contents[1].contents[0].text)
    # print(sec.contents[1].contents[0]['href'])
    # try:
    #     print(sec.contents[1].contents[1].contents[2].text)
    # except:
    #     print("==================================================================")
    restaurants_url.append(sec.contents[1].contents[0]['href'])

r.close()
