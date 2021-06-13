from bs4 import BeautifulSoup
import data_script
import requests
import csv
from statistics import mean

# prompt for URL
print('Paste the full URL of your ebay search results below:')
ebay_url = input('> ')

# retrieve mattress listings from first page on ebay
html_text = requests.get(ebay_url).text
soup = BeautifulSoup(html_text, 'lxml')

# create a list of matresses and store them in items
mattresses = soup.find('ul', class_ = 'srp-results srp-list clearfix')
items = mattresses.find_all('li', class_ = 's-item')

# create empty data list with titles
data = []
data.append(['Product', 'Price'])

# iterate through items, get titles and prices
for item in items:
  link = item.find('a', class_ = 's-item__link')
  product_title = link.find('h3', class_ = 's-item__title').text

  # clean up price list and get average price
  price = item.find('span', class_ = 's-item__price').text.split()
  if len(price) > 1:
    price.remove('to')
  for i in range(len(price)):
    price[i] = price[i].replace('$','').replace(',','')
    price[i] = float(price[i])
  avg_price = mean(price)

  data.append([product_title, avg_price])

with open('results.csv', 'w', encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerows(data)

data_script.pandas_script()
