import time
from threading import Thread
from multiprocessing import Queue
from Get_Page_Html import GetPageHtml


def GetReviews(Tag):
    reviews = []
    review_text = Tag.contents[2]
    for tag in range(0,len(review_text)):
        child_tag = review_text.contents[tag]
        if child_tag.name == 'p':
            if child_tag.text != "": reviews.append(child_tag.text)
    return reviews


def NextButtonCheck(Tag):
    try:
        Tag.contents[3].contents[1].contents[0].contents[5]
        return True
    except:
        return False


reviews = []
def GetReviewsSection(Url):
    global reviews
    one_restaurant_html = GetPageHtml(Url)
    print(Url)
    try:
        review_section = one_restaurant_html.main.contents[0].contents[4].contents[0].contents[0].contents[1]
    except:
        GetReviewsSection(Url)

    reviews = reviews + GetReviews(review_section)


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
        th = Thread(target = GetReviewsSection,args=[review_page_url])
        threads.append(th)
        th.start()

    for i in threads:
        i.join()

    return {'name':restaurant_name,'rating':rating,'reviews':reviews}
   

# print(ScrapReviews("https://www.zomato.com/ncr/local-connaught-place-new-delhi"))
print(ScrapReviews("https://www.zomato.com/ncr/key-hotel-samrat-chanakyapuri-new-delhi"))