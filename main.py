import json

import requests
import selenium
from bs4 import BeautifulSoup

# URL of the page we want to scrape 
#https://www.ttusports.com/general/headlines-featured

# Request the page with url parameter with error handling
def request_page(url):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "*/*",
        }
        response = requests.get(url, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    
# Parse the page with BeautifulSoup
def parse_page(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
    
def extract_image_src(soup):
    images = []
    for span in soup.find_all('span', class_='thumb'):
        img = span.find('img')
        if img and 'src' in img.attrs:
            images.append(img['src'])
    return images

if __name__ == "__main__":
    # print(request_page("https://www.ttusports.com/general/headlines-featured"))
    # print(parse_page(request_page("https://www.ttusports.com/general/headlines-featured")))
    print(extract_image_src(parse_page(request_page("https://www.ttusports.com/general/headlines-featured"))))