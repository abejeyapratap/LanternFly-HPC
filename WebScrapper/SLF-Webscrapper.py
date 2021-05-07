from bs4 import BeautifulSoup as bs
import requests  
from urllib.request import urlopen
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import math


def isValid(u):
    parsed = urlparse(u)
    return bool(parsed.netloc) and bool(parsed.scheme)

def getAllImg(link):
    imgs = []
    ##html_soup = bs(page_html,'html.parser')
    soup = bs(requests.get(link).content, "html.parser")
    ##page = requests.get(link)
    for img in soup.select(selector="img"):

        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(link, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if isValid(img_url):
            imgs.append(img_url)
    
    return imgs



if __name__ == "__main__":
    url_Scrape = "https://www.istockphoto.com/photos/spotted-lanternfly"

    flies = getAllImg(url_Scrape)
    print(flies)
    '''
    req = urlopen(url_Scrape)
    page_html = req.read()
    req.close()

    html_soup = bs(page_html,'html.parser')
    '''
   ##lies = html_soup.find_all('images?q=tbn')

