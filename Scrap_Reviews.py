import time
from threading import Thread
from multiprocessing import Queue
from Get_Page_Html import GetPageHtml
from Get_Sentiment import GetSentiment
import pandas as pd


def GetReviews(Url,Name,Rating):
    one_restaurant_html = GetPageHtml(Url)
    print(Url)
    review_section = None

    try:
        review_section = one_restaurant_html.main.contents[0].contents[4].contents[0].contents[0].contents[1]
    except:
        GetReviews(Url,Name,Rating)
        return

    review_text = review_section.contents[2]
    columns = ['name','rating','reviews','sentiment']
    df = pd.DataFrame(columns = columns)
    for tag in range(0,len(review_text)):
        child_tag = review_text.contents[tag]
        if child_tag.name == 'p':
            if child_tag.text != "":
                # df1 = pd.read_csv('reviews.csv')
                df = df.append({'name': Name,'rating':Rating,'reviews':child_tag.text,
                                'sentiment':GetSentiment(child_tag.text)},ignore_index = True)
                # df = pd.concat([df1,df]).drop_duplicates().reset_index(drop=True)
                df.to_csv('reviews.csv', mode = 'a', header = False, index=False)


def ScrapReviews(Url):
    restaurant_html = GetPageHtml(Url+"/reviews")
    restaurant_name = restaurant_html.main.contents[0].contents[2].find_all('h1')[0].text
    no_of_reviews = restaurant_html.main.contents[0].contents[4].find_all('p')[0].text[13:-1]
    try:
        rating = restaurant_html.main.contents[0].contents[2].find_all('p')[0].text
    except:
        rating = 0

    print(rating)
    threads = []
    for page_no in range(1,int(no_of_reviews)//5+2):
        review_page_url = Url + "/reviews?page="+ str(page_no) +"&sort=dd&filter=reviews-dd"
        th = Thread(target = GetReviews,args=[review_page_url,restaurant_name,rating])
        threads.append(th)
        th.start()

    for i in threads:
        i.join()


    # global reviews
    # return {'name':restaurant_name,'rating':rating,'reviews':reviews}
   
# print(ScrapReviews("https://www.zomato.com/ncr/local-connaught-place-new-delhi"))
# print(ScrapReviews("https://www.zomato.com/ncr/key-hotel-samrat-chanakyapuri-new-delhi"))

# print(pd.read_csv('reviews.csv').drop_duplicates())