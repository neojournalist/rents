import pandas
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.house.kg/snyat-kvartiru?region=1&town=2"
response = requests.get(url)
soup = bs(response.text, 'html.parser')

details = soup.find_all('p', 'title')
list_details =
price = soup.find_all('div', class_='price')
list_price =
date = soup.find_all('div', class_='glyphicon glyphicon-circle-arrow-up')
list_date =

print(details)