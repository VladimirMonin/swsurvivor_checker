"""
# Скрипт который заходит на сайт https://www.gamesvoice.ru/swsurvivor
# И проверяет наличие текста "Этот русификатор пока ещё недоступен"
В элементе //*[@id="comp-lh1g6uej"]/h1/span/span/span/span

Через библиотеку requests и beautifulsoup
# pip install requests
# pip install beautifulsoup4

Скриптовый стиль!

Библиотека для системных уведомлений plyer
# pip install plyer
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
    print('Успех. Сайт доступен')
else:
    print('Ошибка. Сайт недоступен')
    exit()

# Анализируем полученный ответ, с помощью парсера, ищем элемент css Selector #comp-lh1g6uej > h1 > span > span > span > span
html = BeautifulSoup(response.text, 'html.parser')

# Проверяем наличие текста "Этот русификатор пока ещё недоступен" в элементе СSS_SELECTOR
if html.select(CSS_SELECTOR)[0].text == 'Этот русификатор пока ещё недоступен':
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

