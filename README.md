# Weather forecast console

This Python code retrieves weather data from the website *wttr.in* for a list of cities and displays the results in the console. The code uses the requests library to make HTTP requests to the website, and parses the resulting HTML responses to extract the weather data.

### Installation
This code requires Python 3.x and the *requests* library. If you do not have Python installed on your system, you can download it from the official website: https://www.python.org/downloads/. Once you have installed Python, you can install the requests library by running the following command in your terminal:
```
pip install requests
```

### Usage
To use this code, simply run the script in a Python environment such as IDLE or Jupyter Notebook. The script will retrieve weather data for the cities specified in the cities list, and print the results to the console. <br />Example for windows command promt:

```
>python weather.py
```

The output should display the weather forecast for three default cities in Russian language: London, Sheremetyevo, and Cherepovets.
```
Лондон

                Пасмурно
       .--.     +9(6) °C
    .-(    ).   ↘ 4 м/c
   (___.__)__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Сб. 01 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │  _`/"".-.     Местами дождь  │
│   ,\_(   ).   +9(7) °C       │   ,\_(   ).   +7(4) °C       │
│    /(___(__)  ↘ 5-6 м/c      │    /(___(__)  ↓ 4-6 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │      ‘ ‘ ‘ ‘  10 км          │
│     ‘ ‘ ‘ ‘   0.1 мм | 84%   │     ‘ ‘ ‘ ‘   0.1 мм | 73%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Вс. 02 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      +12(10) °C     │      .-.      +5(3) °C       │
│   ― (   ) ―   ↙ 5 м/c        │   ― (   ) ―   ↙ 3-5 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Пн. 03 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │               Пасмурно       │
│      .-.      +12(10) °C     │      .--.     +5(3) °C       │
│   ― (   ) ―   ← 5 м/c        │   .-(    ).   ↙ 2-3 м/c      │
│      `-’      10 км          │  (___.__)__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Шереметьево

   _`/"".-.     Местами дождь
    ,\_(   ).   +4(-1) °C
     /(___(__)  ↑ 6 м/c
       ‘ ‘ ‘ ‘  10 км
      ‘ ‘ ‘ ‘   0.1 мм
                        ┌─────────────┐
┌───────────────────────┤ Сб. 01 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │               Пасмурно       │
│     (   ).    +3(-1) °C      │      .--.     +3(-1) °C      │
│    (___(__)   ↑ 6-8 м/c      │   .-(    ).   ↑ 3-5 м/c      │
│     ‘ ‘ ‘ ‘   2 км           │  (___.__)__)  10 км          │
│    ‘ ‘ ‘ ‘    0.4 мм | 95%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Вс. 02 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Ясно           │
│  _ /"".-.     +10(7) °C      │      .-.      +7(5) °C       │
│    \_(   ).   ↑ 6 м/c        │   ― (   ) ―   ↖ 2-5 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Пн. 03 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │      .-.      Небольшой дожд…│
│      .-.      +12(10) °C     │     (   ).    +6(5) °C       │
│   ― (   ) ―   ← 4-5 м/c      │    (___(__)   ↓ 2-3 м/c      │
│      `-’      10 км          │     ‘ ‘ ‘ ‘   9 км           │
│     /   \     0.0 мм | 0%    │    ‘ ‘ ‘ ‘    2.3 мм | 69%   │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Череповец

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

Все новые фичи публикуются здесь: @igor_chubin
```


You can modify the cities list to retrieve weather data for other cities. You can also modify the PARAMS dictionary to change the options used when making requests to wttr.in. The available options are described in the code comments or you can try to use other keys according to wttr.in documentation [wwwr.in help ](https://wttr.in/:help) 

## `get_forecast` function 
This module also provides a function `get_forecast` that takes in two parameters - `params` and `city`,
and returns a string containing the weather forecast for the specified city using the parameters
defined in `params`.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
