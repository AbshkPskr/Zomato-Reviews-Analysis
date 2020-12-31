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

count = 1
for divs in main_div.children:
    for sec in divs.children:
        print(sec.contents[1].contents[0].text)
        print(sec.contents[1].find('a').text)
        # for tags in sec.children:
        #     for link in tags.children:
        #         print(link)
        count+=1
        # print(str(count)+"_____________________________________________")
    #     if count == 2:
    #         break
    # if count == 2 :
    #     break

# rest_link = main_div.find_all('a')

# print(rest_link[0])
# for rest in range (0,len(rest_link)-1,1):
#     print(rest_link[rest]['href'])

r.close()
