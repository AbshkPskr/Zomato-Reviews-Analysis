import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# r = requests.get("https://www.zomato.com/ncr/top-restaurants",headers = headers)


# soup = BeautifulSoup(r.text,'html.parser')
# restaurants = soup.find('div',{'class':"bke1zw-0 cMipmx"})
# list_tr = restaurants.find_all('a')

# # for restaurant in restaurants:
# #     print(restaurant)

# for i in list_tr:
#     print(list_tr.text)

# # print(restaurants[0].find('a'))

from requests_html import HTMLSession
import re

r = HTMLSession().get("https://www.zomato.com/ncr/top-restaurants",headers = headers)

r.html.render(sleep=1, keep_page = True, scrolldown = 1)

soup = BeautifulSoup(r.text,'html.parser')
main_div = soup.find('div',{'class':"bke1zw-0 cMipmx"})
rest_link = main_div.find_all('a')

print(rest_link[0])
# for rest in rest_link:
#     print(rest['href'])

