import requests


CITIES = ['Лондон', 'Шереметьево', 'Череповец']
PARAMS = {
    'n': '',  # narrow version (only day and night)
    'T': '',  # switch terminal sequences off (no colors)
    'q': '',  # quiet version (no "Weather report" text)
    'm': '',  # metric (SI) (used by default everywhere except US)
    'M': '',  # show wind speed in m/s
    'lang': 'ru',
    }
URL_TEMPLATE = 'https://wttr.in/{}'

def get_forecast(params, city):
    '''returns weather forecast for city with defined params'''
    url = URL_TEMPLATE.format(city)
    response = requests.get(url, params=params, timeout=50)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city in CITIES:
        print(get_forecast(params=PARAMS, city=city))