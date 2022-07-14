import requests
from bs4 import BeautifulSoup
import texttable as tt

# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

page = requests.get(url)
page_soup = BeautifulSoup(page.text, 'html.parser')

# List for data
data = []

# Use iter() to make table iterable
data_iterable = iter(page_soup.findAll('td')) # This will scrape every element of the table

while True:
    try:
        country = next(data_iterable).text
        confirmed = next(data_iterable).text
        deaths = next(data_iterable).text
        continent = next(data_iterable).text

        data.append((country, int(confirmed.replace(',', '')), int(deaths.replace(',', '')), continent))

    except StopIteration:
        break

# Sort the data by the number of confirmed cases
data.sort(key=lambda row: row[1], reverse=True)

# Create texttable
covid_table = tt.Texttable()

# Add empty row at begining for header
covid_table.add_rows([(None, None, None, None)] + data)

covid_table.set_cols_align(('c', 'c', 'c', 'c')) # Aligns cols at center

covid_table.header(('Country', 'Number of Cases', 'Deaths', 'Continent'))

print(covid_table.draw())