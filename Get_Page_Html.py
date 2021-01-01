from bs4 import BeautifulSoup
from requests_html import HTMLSession

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def GetPageHtml(Url):
    page = HTMLSession().get(Url,headers = headers)
    page.html.render()
    html = BeautifulSoup(page.text,'html.parser')
    page.close()
    return html
