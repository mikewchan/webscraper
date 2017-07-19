# https://www.dataquest.io/blog/web-scraping-tutorial-python/

import requests

from bs4 import BeautifulSoup

def search_for_tags_by_class_and_id():
    page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

    # creates an instance of the BeautifulSoup class to parse the document
    soup = BeautifulSoup(page.content, 'html.parser')

    # find any p tag that has the class outer-text
    print(soup.find_all('p', class_='outer-text'))

    # find any tag that has the class outer-text
    print(soup.find_all(class_="outer-text"))

    # find any tag that has the id "first"
    print(soup.find_all(id="first"))

search_for_tags_by_class_and_id()

def using_css_selectors():
    page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.select("div p"))

using_css_selectors()
