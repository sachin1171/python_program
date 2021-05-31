# Setting a goal for the web scraping project

# + Let's take a step back and be sure to clarify our goal.
# + Here is my list of requirements for a succesful web scraping project
# + We are gathering information that is worth the effort it takes to build a working web scraper
# + We are downloading information that can be legally and ehically gathered by web scraper
# + We should have some knowledge of how to find the target information in HTML code
# + We have the right tools: in this case it's libraries Beautiful soup and requests

import requests # for making standard html requests
from bs4 import BeautifulSoup
import json # parsing data
import pandas as pd


page = requests.get("https://www.familydollar.com/locations/id/")
page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')


# + Beautifulsoup will take HTML or XML content and transform it into a complex tree of objects
print(soup.prettify())

dollar_tree_list = soup.find_all('href')


dollar_tree_list


dollar_tree_list = soup.find_all(class_ = 'itemlist')
dollar_tree_list

for i in dollar_tree_list[:2]:
    print(i)

type(dollar_tree_list)


example = dollar_tree_list[2]
example_content = example.contents
example

print(example_content)

# + Use .attr to find what attributes are present in the contents of the object
example_content = example.contents[0]

example_content.attrs

example_href = example_content['href']
example_href

city_hrefs = []

for i in dollar_tree_list:
    cont = i.contents[0]
    href = cont['href']
    city_hrefs.append(href)

for i in city_hrefs[:2]:
    print(i)

city_hrefs

page2 = requests.get(city_hrefs[2])
soup2 = BeautifulSoup(page2.text, 'html.parser')