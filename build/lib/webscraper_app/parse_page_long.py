# https://www.dataquest.io/blog/web-scraping-tutorial-python/

# Imports the requests library that downloads the HTML contents of a page
import requests

# Imports the BeautifulSoup library to parse the document
from bs4 import BeautifulSoup

# Downloads the content from that URL
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# Create an instance of the BeautifulSoup class to parse the document
soup = BeautifulSoup(page.content, 'html.parser')

# Formats the output nicely and prints it
soup.prettify()

# Selects all the elements at the top level of the page using the
# children property of soup. Then we call the list function on it
# because children returns a list generator.
list(soup.children)

# Tells us what the type of each element in the list is.
# We will see 3 types:
# 1) a Doctype object (contains info about the type of doc),
# 2)a NavigableString, which represents text found in the HTML doc,
# 3) a Tag object, which contains other nested tags. This is the most important.
[type(item) for item in list(soup.children)]

# Selects the html tag and its children by taking the third item in the list
html = list(soup.children)[2]

# Finds the children inside the html tag.
list(html.children)

# We want to extract the text inside the p tag, so we dive into the body.
# We select the body tag and its children by taking the 4th item in the list.
# The first three items are the \n, the head tag, and another \n.
body = list(html.children)[3]

# Now we can get the p tag by finding the children of the body tag.
list(body.children)

# Now we isolate the p tag by pulling the 2nd item in the list
p = list(body.children)[1]

# We can now use the get_text method to extract all of the text inside the tag
print(p.get_text())
