import requests

from bs4 import BeautifulSoup

def find_all_instances_tag():
    page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

    # We can use the find_all method to find all the instances of a tag on a page.
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.find_all('p')

    # find_all returns a list, so we'll have to loop through or use list indexing
    # to extract text
    print(soup.find_all('p')[0].get_text())

    # If you only want to find the first instance of a tag, you can use the
    # find method, which will return a single BeautifulSoup object
    print(soup.find('p'))
