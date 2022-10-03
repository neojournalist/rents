import pandas
import requests
from bs4 import BeautifulSoup as bs
import xml

# def upload():
url = "https://stroka.kg/snyat-kvartiru/?q=&order=cost&cost_min_som=&cost_max_som=&topic_point=bishkek&p=0#paginator"
response = requests.get(url)
soup = bs(response.text, 'html.parser')
#print(response)

#items = soup.find_all('tr', class_="topics-item-tr topics-item-tr-title")
prices = soup.find('td', class_='topics-item-topic_cost topics-item-td')
rooms = soup.find_all('td', 'topics-item-td topics-item-topic_rooms')
series = soup.find_all('td', class_='topics-item-topic_series topics-item-td')
content = soup.find_all('a', class_='topics-item-view')

list_prices = [int(prices.text) for price in prices]
print(list_prices)
#list_prices = [prices.text for price in prices]
#print(list_prices)

# for i in prices:
#     list_prices = [i.text for price in prices]
#     print(list_prices)

# for p,r,s,c in enumerate(items, start=1):
#     price = p.find('td', class_='topics-item-topic_cost topics-item-td  som').text
#     rooms = int(r.find('td', class_='topics-item-td topics-item-topic_rooms').text)
#     series = s.find('td', class_='topics-item-topic_series topics-item-td').text
#     content = c.find('a', class_='topics-item-view').text
#
# print(price)


