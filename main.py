"""
# Скрипт который заходит на сайт https://www.gamesvoice.ru/swsurvivor
# И проверяет наличие текста "Этот русификатор пока ещё недоступен"
В элементе //*[@id="comp-lh1g6uej"]/h1/span/span/span/span

Через библиотеку requests и beautifulsoup
# pip install requests
# pip install beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup