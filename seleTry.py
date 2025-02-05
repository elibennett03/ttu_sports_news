import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# URL of the page we want to scrape
URL = "https://www.ttusports.com/general/headlines-featured"

# Set up Selenium WebDriver
def setup_driver():
    options = Options()
    options.headless = True  # Run in headless mode (no UI)
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Helps avoid bot detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    return driver

# Scroll the page to trigger lazy loading
def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Request the page using Selenium
def request_page(url):
    driver = setup_driver()
    driver.get(url)
    time.sleep(3)  # Allow time for initial page load
    scroll_page(driver)  # Scroll to trigger lazy loading
    page_source = driver.page_source
    driver.quit()
    return page_source

# Parse the page with BeautifulSoup
def parse_page(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

# Extract images from parsed page
def extract_image_src(soup):
    images = []
    for span in soup.find_all('span', class_='thumb'):
        img = span.find('img')
        if img and 'src' in img.attrs:
            images.append(img['src'])
    return images

# Extract titles from articles
def extract_titles(soup):
    titles = []
    for span in soup.find_all('span', class_='thumb'):
        img = span.find('img')
        if img and 'src' in img.attrs:
            images.append(img['src'])
    return titles

if __name__ == "__main__":
    page_source = request_page(URL)
    soup = parse_page(page_source)
    images = extract_image_src(soup)
    titles = extract_titles(soup)
    print(images)
    print(titles)

#https://www.ttusports.com/general/2024-25/photos/2024-25_Tennessee_Tech_AD_Honor_Roll_Fall_-24.jpg?max_width=400&useS3=true