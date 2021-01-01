from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def NextButtonCheck(Tag):
    try:
        Tag.contents[3].contents[1].contents[0].contents[6]
        return True
    except:
        return False

def GetComments(Tag):
    review_text = Tag.contents[2]
    for tag in range(0,len(review_text)):
        child_tag = review_text.contents[tag]
        if child_tag.name == 'p':
            if child_tag.text != "":
                print(child_tag.text)


def ScrapReviews(urls):
    for url in urls:
        OneRestauantHtml = HTMLSession().get(url,headers = headers)
        OneRestauantHtml.html.render()
        soup = BeautifulSoup(OneRestauantHtml.text,'html.parser')
        restaurant_name = soup.main.contents[0].contents[2].find_all('h1')[0].text
        no_of_reviews = soup.main.contents[0].contents[4].find_all('p')[0].text
        
        for page_no in range(1,10):
            review_page_url = url + "/reviews?page="+ str(page_no) +"&sort=dd&filter=reviews-dd"
            OneRestauantHtml = HTMLSession().get(review_page_url,headers = headers)
            OneRestauantHtml.html.render()

            soup = BeautifulSoup(OneRestauantHtml.text,'html.parser')
            review_section = soup.main.contents[0].contents[4].contents[0].contents[0].contents[1]

            GetComments(review_section)

            next_button_check = None
            if page_no > 1:
                if NextButtonCheck(review_section) == False:
                    OneRestauantHtml.close()
                    break

            time.sleep(1)
            OneRestauantHtml.close()

ScrapReviews(["https://www.zomato.com/ncr/bo-tai-switch-connaught-place-new-delhi"])
