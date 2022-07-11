import datetime
import urllib.request
import json

url = 'https://tum-dev.github.io/eat-api/mensa-garching/' + str(datetime.date.today().year) + '/'\
		+ str(datetime.date.today().isocalendar()[1]) + '.json'

def parse():
    with urllib.request.urlopen(url) as openUrl:
        data = json.loads(openUrl.read().decode())

    for day in data['days']:
        if day['date'] == datetime.date.today().strftime('%Y-%m-%d'):
            break

    food = []
    for dish in day['dishes']:
        if dish['dish_type'] == 'Beilagen':
            break
        food.append(dish)


    bei = []
    for dish in day['dishes']:
        if dish['dish_type'] == 'Beilagen':
            bei.append(dish)

    map
    bei.pop('prices')
    return food, bei

food, bei = parse()

print('fertig')