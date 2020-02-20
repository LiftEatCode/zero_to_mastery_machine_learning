# Import Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#specify URl
url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text

# Parse the HTML from our URL into the BeautifulSoup parse tree format
soup = BeautifulSoup(url, "lxml")

# To look at the HTML underlying to the web
#print(soup.prettify())

# to get the title of the page
soup.title()

# use the 'find_all' function to bring back all instances of the 'table'
# tag in the HTML and store in 'all_tables' variable

all_tables = soup.find_all("table")
all_tables

# use the 'find_all' function to bring back all instances of the 'table' 
# tag in the HTML and store in 'all_tables' variable

my_table = soup.find('table', {'class': 'wikitable sortable'})
my_table

links = my_table.find_all('a')
links

# From the URL, we have to extract the title which is the name of countries.
countries = []
for link in links:
	countries.append(link.get('title'))

countries

# convert countries into a panda dataframe
df = pd.DataFrame()
df['Country'] = countries
print(df)
