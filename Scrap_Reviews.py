import time
from threading import Thread
from multiprocessing import Queue
from Get_Page_Html import GetPageHtml
from Get_Sentiment import GetSentiment
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime
import re

import time
start_time = time.time()

def ConvertDate(ago):
    try: 
        value, unit = re.search(r'(\d+) (\w+) ago', ago).groups()
        if not unit.endswith('s'):
            unit += 's'
        delta = relativedelta(**{unit: int(value)})
        date = datetime.now() - delta
        return pd.to_datetime(date)
    except: 
        pass
    try:
        return pd.to_datetime(ago)
    except:
        return ''

def GetReviews(Url,Name,Rating):
    one_restaurant_html = GetPageHtml(Url)
    review_section = None

    try:
        review_section = one_restaurant_html.main.contents[0].contents[4].contents[0].contents[0].contents[1]
    except:
        GetReviews(Url,Name,Rating)
        return

    review_text = review_section.contents[2]
    date = ''
    customer_rating = 0
    review = None
    sentiment = 0

    for tag in range(0,len(review_text)):
        df = pd.DataFrame(columns = ['name','rating','date','cust_rating',
                                    'reviews','sentiment'])
        child_tag = review_text.contents[tag]

        if child_tag.name == 'div' and child_tag.text != '':
            try:
                customer_rating = float(child_tag.text[0:3])
                date = ConvertDate(child_tag.text[3:])
            except:
                continue

        if child_tag.name == 'p':# and child_tag.text != '':
            review = child_tag.text

        if date != '' and review != None:
            if review == '':
                sentiment = (2*(float(customer_rating)/5)) - 1
            else:
                sentiment = GetSentiment(review)
            df = df.append({'name': Name,'rating':Rating,'date':date,
                            'cust_rating':customer_rating,'reviews':review,
                            'sentiment':sentiment},ignore_index = True)
            df.to_csv('reviews.csv', mode = 'a', header = False, index=False)
            # print(date)
            # print(review,"===========================")
            review = None

            
def ScrapReviews(Url):
    restaurant_html = GetPageHtml(Url+"/reviews")
    restaurant_name = restaurant_html.main.contents[0].contents[2].find('h1').text
    no_of_reviews = restaurant_html.main.contents[0].contents[4].find('p').text[13:-1]
    try:
        rating = restaurant_html.main.contents[0].contents[2].find('p').text
    except:
        rating = 0

    threads = []
    for page_no in range(1,int(no_of_reviews)//5+2):
        print(restaurant_name,"-----",page_no)
        review_page_url = Url + "/reviews?page="+ str(page_no) +"&sort=dd&filter=reviews-dd"
        # GetReviews(review_page_url,restaurant_name,rating)
        th = Thread(target = GetReviews,args=[review_page_url,restaurant_name,rating])
        th.start()
        threads.append(th)
        # print("len of threads-- ",len(threads),th.name )
        if len(threads) > 10:
            for thrd in threads:
                thrd.join()
            threads = []
        # return
    
    pd.read_csv('reviews.csv').drop_duplicates().to_csv('reviews.csv',index= False)
   


# print(ScrapReviews("https://www.zomato.com/ncr/local-connaught-place-new-delhi"))
# print(ScrapReviews("https://www.zomato.com/ncr/key-hotel-samrat-chanakyapuri-new-delhi"))
# print(ScrapReviews("https://www.zomato.com/ncr/the-potbelly-chanakyapuri-new-delhi"))


print("--- %s seconds ---" % (time.time() - start_time))