import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://stroka.kg/snyat-kvartiru/?q&order=date_up&cost_min_som&cost_max_som&topic_point=bishkek"
response = requests.get(url)
soup = bs(response.text, 'html.parser')


prices = soup.find_all('td', class_='topics-item-topic_cost topics-item-td')
prices_list = [p.text for p in prices]
rooms = soup.find_all('td', class_='topics-item-td topics-item-topic_rooms')
rooms_list = [r.text for r in rooms]
dates = soup.find_all('td', class_='topics-item-td topics-item-topic_date_create')
dates_list = [d.text for d in dates]
#series = soup.find_all('td', class_='topics-item-topic_series topics-item-td')
#series_list = [s.text for s in series]
#prices_list.extend(rooms_list)
print(len(dates_list))
print(len(rooms_list))
print(len(prices_list))


# prod_info = pd.DataFrame(
#       {
#           'price': prices_list,
#
#       })
# # #
# a = {'Links' : lines ,'Titles' : titles , 'Singers': finalsingers , 'Albums':finalalbums , 'Years' : years}
# df = pd.DataFrame.from_dict(a, orient='index')
# df = df.transpose()
# prod_info.to_csv('flats.csv', index=False)
# print('Файл загружен!')
# for p in prices:
#     list_prices = [int(p.text[:-2])]
#     print(list_prices)
#
# for r in rooms:
#     list_rooms = [r.text]
#     print(list_rooms)
#
# for s in series:
#     list_series = [s.text]

