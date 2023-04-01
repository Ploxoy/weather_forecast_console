"""
A module for fetching weather forecast from wttr.in API.

This module provides a function `get_forecast` that takes in two parameters - `params` and `city`,
and returns a string containing the weather forecast for the specified city using the parameters
defined in `params`.

The `params` parameter is a dictionary containing the following keys:
- 'n': narrow version (only day and night)
- 'T': switch terminal sequences off (no colors)
- 'q': quiet version (no "Weather report" text)
- 'm': metric (SI) (used by default everywhere except US)
- 'M': show wind speed in m/s
- 'lang': language of the forecast (default is 'en')

Example usage:

    from weather_forecast import get_forecast

    params = {
        'n': '',
        'T': '',
        'q': '',
        'm': '',
        'M': '',
        'lang': 'ru',
    }

    city = 'Moscow'

    forecast = get_forecast(params=params, city=city)

    print(forecast)

Output:
Москва, Россия

     \  /       Переменная облачность
   _ /"".-.     +4(3) °C
     \_(   ).   ↓ 1 м/c
     /(___(__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Сб. 01 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │               Дымка          │
│      .--.     +3(2) °C       │  _ - _ - _ -  0(-3) °C       │
│   .-(    ).   ↓ 1 м/c        │   _ - _ - _   ↖ 2-4 м/c      │
│  (___.__)__)  10 км          │  _ - _ - _ -  2 км           │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Вс. 02 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Небольшой дожд…│               Туман          │
│     (   ).    +2(0) °C       │  _ - _ - _ -  +1(-2) °C      │
│    (___(__)   ↖ 1-3 м/c      │   _ - _ - _   ↘ 2-3 м/c      │
│     ‘ ‘ ‘ ‘   9 км           │  _ - _ - _ -  0 км           │
│    ‘ ‘ ‘ ‘    1.6 мм | 61%   │               0.1 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Пн. 03 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Умеренный снег │  _`/"".-.     Небольшой снег │
│     (   ).    0(-5) °C       │   ,\_(   ).   0(-5) °C       │
│    (___(__)   ↓ 4-6 м/c      │    /(___(__)  ↓ 4-6 м/c      │
│    * * * *    5 км           │      *  *  *  10 км          │
│   * * * *     0.2 мм | 0%    │     *  *  *   0.1 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
"""
import requests


URL_TEMPLATE = 'https://wttr.in/{}'
DEFAULT_CITIES = ['Лондон', 'Шереметьево', 'Череповец']
DEFAULT_PARAMS = {
    'n': '',  # narrow version (only day and night)
    'T': '',  # switch terminal sequences off (no colors)
    'q': '',  # quiet version (no "Weather report" text)
    'm': '',  # metric (SI) (used by default everywhere except US)
    'M': '',  # show wind speed in m/s
    'lang': 'ru',
}


def get_forecast(params, city=None):
    '''Returns the weather forecast for the specified city with the specified parameters

    Args:
    params (dict): The dictionary with the query parameters
    city (str): The name of the city to retrieve the forecast for

    Returns:
    str: The text response of the HTTP request to the wttr.in API

    Raises:
    HTTPError: An error occurred accessing the wttr.in API
    '''
    url = URL_TEMPLATE.format(city)
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city_ in DEFAULT_CITIES:
        print(get_forecast(params=DEFAULT_PARAMS, city=city_))
