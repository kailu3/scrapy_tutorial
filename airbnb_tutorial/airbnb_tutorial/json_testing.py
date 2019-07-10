import json
import time
import pprint
import collections

with open('first_page.json', 'r') as file:
    data = json.load(file)

homes = data.get('explore_tabs')[0].get('sections')[3].get('listings')

BASE_URL = 'https://www.airbnb.com/rooms/'

data_dict = collections.defaultdict(dict)
for home in homes:
    room_id = str(home.get('listing').get('id'))
    data_dict[room_id]['url'] = BASE_URL + str(home.get('listing').get('id'))
    data_dict[room_id]['price'] = home.get('pricing_quote').get('rate').get('amount')
    data_dict[room_id]['avg_rating'] = home.get('listing').get('avg_rating')
    data_dict[room_id]['reviews_count'] = home.get('listing').get('reviews_count')

printer = pprint.PrettyPrinter()
printer.pprint(data_dict)