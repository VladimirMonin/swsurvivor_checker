"""
Проверяем, вышла ли русская локализация для игры Star Wars Jedi: Survivor

Скрипт который заходит на сайт https://www.gamesvoice.ru/swsurvivor
И проверяет наличие текста "Этот русификатор пока ещё недоступен"

Через библиотеку requests и beautifulsoup

Так же, используется библиотека plyer для отправки уведомлений на рабочий стол
Библиотека для системных уведомлений plyer

И библиотека webbrowser для открытия сайта в браузере, в случае если русификатор доступен.

После, скрипт упаковывается в exe файл с помощью pyinstaller, флаги описаны в README.md
"""

import requests
from bs4 import BeautifulSoup
from plyer import notification
import webbrowser

URL = r'https://www.gamesvoice.ru/swsurvivor'
XPATH = r'//*[@id="comp-lh1g6uej"]/h1/span/span/span/span'
CSS_SELECTOR = r"#comp-lh1g6uej > h1 > span > span > span > span"
MESSAGE = None

# Делаем GET запрос на сайт
response = requests.get(URL)

# Проверяем статус ответа
if response.status_code == 200:
    print('Сайт доступен')
else:
    print('Ошибка. Сайт недоступен')
    exit()

# Получаем HTML из ответа
html = response.text

# Создаем объект BeautifulSoup для возможности парсинга данных из HTML
bs4 = BeautifulSoup(html, 'html.parser')

# Проверяем наличие текста "Этот русификатор пока ещё недоступен" в элементе СSS_SELECTOR
# Метод select возращает список элементов, поэтому обращаемся к первому элементу
if bs4.select(CSS_SELECTOR)[0].text == 'Этот русификатор пока ещё недоступен':
    print('Русификатор еще не доступен')

    MESSAGE = 'Русификатор еще не доступен'

else:
    print('Русификатор доступен')
    MESSAGE = 'Русификатор доступен'
    webbrowser.open(URL)  # Открываем сайт


# Отправляем уведомление
notification.notify(
    title=f'Star Wars Jedi: Survivor: {MESSAGE}',
    message=MESSAGE,
    app_name='GamesVoice',
    app_icon='icon.ico',
    timeout=10
)

