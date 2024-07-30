#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import bs4

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

# Mock HTML content simulating a local weather page
html_content = """
<html>
<head>
    <title>Local Weather</title>
</head>
<body>
    <div id="weather">
        <h2>Today's Weather</h2>
        <p>Temperature: <span class="temp">25°C</span></p>
        <p>Condition: <span class="condition">Sunny</span></p>
        <p>Humidity: <span class="humidity">60%</span></p>
    </div>
</body>
</html>
"""

# Parse the HTML content using Beautiful Soup
soup = bs4.BeautifulSoup(html_content, 'html.parser')

# Extract the weather information
temperature = soup.find('span', class_='temp').text
condition = soup.find('span', class_='condition').text
humidity = soup.find('span', class_='humidity').text

# Print the extracted information
print(f"Temperature: {temperature}")
print(f"Condition: {condition}")
print(f"Humidity: {humidity}")
