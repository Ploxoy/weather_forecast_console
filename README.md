
This Python code retrieves weather data from the website wttr.in for a list of cities and displays the results in the console. The code uses the requests library to make HTTP requests to the website, and parses the resulting HTML responses to extract the weather data.

Installation
This code requires Python 3.x and the requests library. If you do not have Python installed on your system, you can download it from the official website: https://www.python.org/downloads/. Once you have installed Python, you can install the requests library by running the following command in your terminal:

Copy code
pip install requests
Usage
To use this code, simply run the script in a Python environment such as IDLE or Jupyter Notebook. The script will retrieve weather data for the cities specified in the cities list, and print the results to the console.

You can modify the cities list to retrieve weather data for other cities. You can also modify the PARAMS dictionary to change the options used when making requests to wttr.in. The available options are described in the code comments.
